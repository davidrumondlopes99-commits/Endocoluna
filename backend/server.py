from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import uuid
from pathlib import Path
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime, timezone

from articles_data import ARTICLES

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

mongo_url = os.environ["MONGO_URL"]
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ["DB_NAME"]]

app = FastAPI(title="NeuroSaúde Blog API")
api_router = APIRouter(prefix="/api")


# -------- Models --------
class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    slug: str
    title: str
    excerpt: str
    category: str  # brain | spine | prevention
    category_label: str
    image_url: str
    reading_time: int
    published_at: str
    author: str
    content_html: str
    views: int = 0


class ArticleSummary(BaseModel):
    id: str
    slug: str
    title: str
    excerpt: str
    category: str
    category_label: str
    image_url: str
    reading_time: int
    published_at: str
    author: str
    views: int = 0


class NewsletterSignup(BaseModel):
    email: EmailStr
    name: Optional[str] = None


class NewsletterResponse(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    subscribed_at: str


# -------- Seed --------
@app.on_event("startup")
async def seed_articles():
    existing = await db.articles.count_documents({})
    if existing == 0:
        await db.articles.insert_many(
            [{**a, "id": str(uuid.uuid4()), "views": 0} for a in ARTICLES]
        )
        logger.info("Seeded %d articles", len(ARTICLES))
    # ensure newsletter unique index
    await db.newsletter.create_index("email", unique=True)


# -------- Routes --------
@api_router.get("/")
async def root():
    return {"message": "NeuroSaúde API ok"}


CATEGORY_MAP = {
    "brain": "Cérebro",
    "spine": "Coluna",
    "prevention": "Prevenção",
}


@api_router.get("/articles", response_model=List[ArticleSummary])
async def list_articles(
    category: Optional[str] = None,
    q: Optional[str] = None,
    limit: int = 20,
):
    query = {}
    if category and category in CATEGORY_MAP:
        query["category"] = category
    if q:
        regex = {"$regex": q, "$options": "i"}
        query["$or"] = [
            {"title": regex},
            {"excerpt": regex},
            {"content_html": regex},
        ]
    cursor = db.articles.find(query, {"_id": 0, "content_html": 0}).limit(limit)
    docs = await cursor.to_list(length=limit)
    docs.sort(key=lambda d: d.get("published_at", ""), reverse=True)
    return docs


@api_router.get("/articles/most-read", response_model=List[ArticleSummary])
async def most_read(limit: int = 5):
    cursor = (
        db.articles.find({}, {"_id": 0, "content_html": 0})
        .sort("views", -1)
        .limit(limit)
    )
    return await cursor.to_list(length=limit)


@api_router.get("/articles/featured", response_model=ArticleSummary)
async def featured():
    doc = await db.articles.find_one({}, {"_id": 0, "content_html": 0}, sort=[("published_at", -1)])
    if not doc:
        raise HTTPException(404, "No articles available")
    return doc


@api_router.get("/articles/{slug}", response_model=Article)
async def get_article(slug: str):
    doc = await db.articles.find_one({"slug": slug}, {"_id": 0})
    if not doc:
        raise HTTPException(404, "Article not found")
    await db.articles.update_one({"slug": slug}, {"$inc": {"views": 1}})
    doc["views"] = doc.get("views", 0) + 1
    return doc


@api_router.get("/categories")
async def get_categories():
    return [
        {"slug": "brain", "label": "Cérebro", "description": "Neurocirurgia e doenças do encéfalo"},
        {"slug": "spine", "label": "Coluna", "description": "Cirurgia de coluna e patologias vertebrais"},
        {"slug": "prevention", "label": "Prevenção", "description": "Saúde, ergonomia e bem-estar"},
    ]


@api_router.post("/newsletter", response_model=NewsletterResponse)
async def newsletter_signup(payload: NewsletterSignup):
    existing = await db.newsletter.find_one({"email": payload.email})
    if existing:
        raise HTTPException(409, "E-mail já cadastrado na newsletter.")
    doc = {
        "id": str(uuid.uuid4()),
        "email": payload.email,
        "name": payload.name,
        "subscribed_at": datetime.now(timezone.utc).isoformat(),
    }
    await db.newsletter.insert_one(doc)
    doc.pop("_id", None)
    return doc


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
