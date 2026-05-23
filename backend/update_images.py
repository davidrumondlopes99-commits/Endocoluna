"""Script que atualiza a imagem de cada artigo no MongoDB com uma imagem única do Unsplash, relevante ao tema. Idempotente."""
import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

U = "https://images.unsplash.com"
QS = "?w=1200&q=80&auto=format&fit=crop"


def u(photo_id):
    return f"{U}/photo-{photo_id}{QS}"


# Curated mapping: each article slug -> unique relevant Unsplash image
IMAGE_MAP = {
    # --- 3 artigos originais ---
    "hernia-de-disco-sintomas-causas-e-quando-a-cirurgia-e-necessaria": u("1559757148-5c350d0d3c56"),
    "aneurisma-cerebral-sintomas-fatores-de-risco-e-tratamentos": u("1559757175-0eb30cd8c063"),
    "dor-nas-costas-constante-como-diferenciar-dor-muscular-de-problema-grave": u("1571019613454-1cb2f99b2d8b"),

    # --- Coluna (spine) ---
    "lombalgia-cronica-causas-e-tratamento": u("1591343395082-e120087004b4"),
    "nervo-ciatico-inflamado-sintomas-e-tratamento": u("1532187863486-abf9dbad1b69"),
    "hernia-de-disco-cervical-sintomas-tratamento": u("1576091160550-2173dba999ef"),
    "bico-de-papagaio-osteofitos-coluna": u("1530026405186-ed1f139313f8"),
    "escoliose-em-adultos-causas-tratamento": u("1599901860904-17e6ed7083a0"),
    "estenose-de-canal-lombar-sintomas-cirurgia": u("1488751045188-3c55bbf9a3fa"),
    "espondilolistese-tratamento": u("1581595220892-b0739db3ba8c"),
    "artrose-facetaria-tratamento": u("1581595219315-a187dd40c322"),
    "sindrome-do-piriforme-falsa-ciatica": u("1574680096145-d05b474e2155"),
    "cirurgia-endoscopica-de-coluna": u("1551601651-2a8555f1a136"),
    "microdiscectomia-cirurgia-hernia-disco": u("1551076805-e1869033e561"),
    "bloqueio-facetario-procedimento": u("1583912267550-d6c2ac3196c0"),
    "mielopatia-cervical-sinais-tratamento": u("1559757148-5c350d0d3c56"),
    "fratura-vertebral-osteoporose-tratamento": u("1559149665-3bfacbc0bf61"),
    "discopatia-degenerativa-tratamento": u("1582719508461-905c673771fd"),
    "espondilite-anquilosante-sintomas": u("1606857521015-7f9fcf423740"),
    "ressonancia-magnetica-coluna-quando-fazer": u("1583912267550-d6c2ac3196c0"),
    "endoscopia-transforaminal-vs-interlaminar": u("1612531048118-826d8c8d8c5b"),
    "sindrome-cauda-equina-emergencia": u("1519494026892-80bbd2d6fd0d"),
    "espondilodiscite-infeccao-coluna": u("1631549916768-4119b4220292"),
    "tumor-de-coluna-sinais-alerta": u("1582719471384-894fbb16e074"),
    "coccigodinia-dor-cocci": u("1521737604893-d14cc237f11d"),
    "lombalgia-em-atletas-prevencao": u("1517999144091-3d9dca6d1e43"),
    "sindrome-facetaria-cervical": u("1559757175-0eb30cd8c063"),
    "dor-toracica-de-coluna": u("1626202373081-6d27f7d05ec3"),
    "sindrome-desfiladeiro-toracico": u("1599134842279-fe807d23316e"),
    "bursite-trocanterica-vs-ciatalgia": u("1571019613454-1cb2f99b2d8b"),
    "hipertrofia-ligamento-amarelo": u("1559757148-5c350d0d3c56"),
    "failed-back-surgery-syndrome": u("1579684385127-1ef15d508118"),
    "espondilolise-defeito-pars": u("1517466787929-bc90951d0974"),
    "siringomielia-cavidade-medula": u("1559757175-0eb30cd8c063"),
    "vertebroplastia-cifoplastia": u("1612531385446-f7e6d131e1d0"),
    "neuroestimulacao-medular-dor-cronica": u("1581595219315-a187dd40c322"),
    "cirurgia-robotica-em-coluna": u("1581094794329-c8112a89af12"),
    "ozonioterapia-para-hernia-de-disco": u("1583912267550-d6c2ac3196c0"),

    # --- Cérebro (brain) ---
    "malformacao-de-chiari": u("1559757175-0eb30cd8c063"),
    "cefaleia-cervicogenica-dor-cabeca-coluna": u("1559757175-0eb30cd8c063"),
    "tontura-cervicogenica": u("1532012197267-da84d127e765"),

    # --- Prevenção ---
    "hiperlordose-lombar": u("1545205597-3d9d02c29597"),
    "cifose-postural-hipercifose-tratamento": u("1571902943202-507ec2618e8f"),
    "retificacao-cervical-causas-tratamento": u("1591343395082-e120087004b4"),
    "dor-lombar-na-gestacao-cuidados": u("1559757175-3a02b1e7b04b"),
    "dor-lombar-aguda-o-que-fazer-primeiras-48-horas": u("1571019613454-1cb2f99b2d8b"),
    "crioterapia-termoterapia-dor-coluna": u("1599901860904-17e6ed7083a0"),
    "acupuntura-para-coluna-evidencias": u("1571942676516-bcab84649e44"),
    "quiropraxia-mitos-e-verdades": u("1574680096145-d05b474e2155"),
    "colete-ortopedico-quando-usar": u("1583912267550-d6c2ac3196c0"),
    "tracao-lombar-cervical": u("1597764690523-15bdcdff4534"),
    "tens-para-dor-coluna": u("1622253692010-333f2da6031d"),
    "cigarro-e-coluna": u("1527613426441-4da17471b66d"),
    "obesidade-e-dor-lombar": u("1607962837359-5e7e89f86776"),
    "postura-home-office-guia-completo": u("1521737604893-d14cc237f11d"),
    "colchao-e-travesseiro-ideal-coluna": u("1631815587646-b85a1bb027e1"),
    "mochila-escolar-coluna-criancas": u("1503676260728-1c00da094a0b"),
    "salto-alto-e-coluna": u("1543163521-1bf539c55dd2"),
    "como-levantar-peso-correto": u("1517836357463-d25dfeac3438"),
    "dor-lombar-e-estresse-mente-corpo": u("1499209974431-9dddcece7f88"),
    "fibromialgia-x-problemas-coluna": u("1532187863486-abf9dbad1b69"),
    "sindrome-dor-miofascial-pontos-gatilho": u("1532187863486-abf9dbad1b69"),
    "pilates-rpg-coluna-evidencias-cientificas": u("1599901860904-17e6ed7083a0"),
    "dor-coluna-em-idosos": u("1488751045188-3c55bbf9a3fa"),
    "lombalgia-no-trabalho-prevencao": u("1521737604893-d14cc237f11d"),
    "alimentacao-e-saude-coluna": u("1490645935967-10de6ba17061"),
    "yoga-para-coluna-beneficios-cuidados": u("1545205597-3d9d02c29597"),
    "primeiros-sinais-problema-coluna": u("1505751172876-fa1923c5c528"),
    "exercicios-fortalecimento-core-coluna": u("1571902943202-507ec2618e8f"),
}


async def run():
    client = AsyncIOMotorClient(os.environ["MONGO_URL"])
    db = client[os.environ["DB_NAME"]]
    updated = 0
    not_found = []
    for slug, image_url in IMAGE_MAP.items():
        r = await db.articles.update_one(
            {"slug": slug}, {"$set": {"image_url": image_url}}
        )
        if r.matched_count:
            updated += 1
        else:
            not_found.append(slug)
    print(f"Updated: {updated}/{len(IMAGE_MAP)}")
    if not_found:
        print("Not found slugs:")
        for s in not_found:
            print(f"  - {s}")
    # also list articles still using the old assets URL
    cursor = db.articles.find(
        {"image_url": {"$regex": "static.prod-images.emergentagent"}},
        {"slug": 1, "_id": 0},
    )
    leftovers = [d["slug"] async for d in cursor]
    if leftovers:
        print(f"Articles still with old image: {len(leftovers)}")
        for s in leftovers:
            print(f"  - {s}")


asyncio.run(run())
