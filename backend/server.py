from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import Response
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
from articles_more import EXTRA_ARTICLES
from articles_more2 import EXTRA_ARTICLES_2
from articles_more3 import EXTRA_ARTICLES_3

ALL_ARTICLES = ARTICLES + EXTRA_ARTICLES + EXTRA_ARTICLES_2 + EXTRA_ARTICLES_3

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
    # Idempotent seed: insert articles whose slug doesn't exist yet
    existing_slugs = set()
    async for doc in db.articles.find({}, {"slug": 1, "_id": 0}):
        existing_slugs.add(doc["slug"])

    new_docs = [
        {**a, "id": str(uuid.uuid4()), "views": 0}
        for a in ALL_ARTICLES
        if a["slug"] not in existing_slugs
    ]
    if new_docs:
        await db.articles.insert_many(new_docs)
        logger.info("Seeded %d new articles", len(new_docs))

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
    limit: int = 100,
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
    cursor = db.articles.find(query, {"_id": 0, "content_html": 0}).sort("published_at", -1).limit(limit)
    return await cursor.to_list(length=limit)


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


@api_router.get("/sitemap.xml")
async def sitemap():
    base = os.environ.get("PUBLIC_SITE_URL", "https://neuroeduca.preview.emergentagent.com")
    urls = [
        {"loc": f"{base}/", "priority": "1.0", "changefreq": "daily"},
        {"loc": f"{base}/sobre", "priority": "0.7", "changefreq": "monthly"},
        {"loc": f"{base}/categoria/spine", "priority": "0.9", "changefreq": "weekly"},
        {"loc": f"{base}/categoria/brain", "priority": "0.9", "changefreq": "weekly"},
        {"loc": f"{base}/categoria/prevention", "priority": "0.9", "changefreq": "weekly"},
    ]
    async for doc in db.articles.find({}, {"slug": 1, "published_at": 1, "_id": 0}).sort("published_at", -1):
        urls.append({
            "loc": f"{base}/artigo/{doc['slug']}",
            "lastmod": doc.get("published_at", ""),
            "priority": "0.8",
            "changefreq": "monthly",
        })

    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml.append("  <url>")
        xml.append(f"    <loc>{u['loc']}</loc>")
        if u.get("lastmod"):
            xml.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        xml.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        xml.append(f"    <priority>{u['priority']}</priority>")
        xml.append("  </url>")
    xml.append("</urlset>")
    return Response(content="\n".join(xml), media_type="application/xml")


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


# YouTube channel feed cache
_youtube_cache = {"data": None, "ts": 0}


@api_router.get("/youtube/videos")
async def youtube_videos(limit: int = 6):
    """Fetch latest videos from Dr. Matheus Lopes' YouTube channel (RSS, cached 1h)."""
    import time
    import re
    import urllib.request

    now = time.time()
    if _youtube_cache["data"] and now - _youtube_cache["ts"] < 3600:
        return _youtube_cache["data"][:limit]

    channel_id = "UCmYFo7gtwGENIKl0ARORRnQ"
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        xml = urllib.request.urlopen(req, timeout=8).read().decode("utf-8")
    except Exception as e:
        logger.warning("YouTube RSS fetch failed: %s", e)
        return _youtube_cache["data"][:limit] if _youtube_cache["data"] else []

    entries = re.findall(
        r"<yt:videoId>([^<]+)</yt:videoId>.*?<title>([^<]+)</title>.*?<published>([^<]+)</published>",
        xml, re.DOTALL,
    )
    videos = [
        {
            "id": vid,
            "title": title,
            "published_at": pub,
            "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
            "url": f"https://www.youtube.com/watch?v={vid}",
            "embed_url": f"https://www.youtube.com/embed/{vid}",
        }
        for vid, title, pub in entries
    ]
    _youtube_cache["data"] = videos
    _youtube_cache["ts"] = now
    return videos[:limit]


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
