"""Backend tests for NeuroSaúde blog API."""
import os
import uuid
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://neuroeduca.preview.emergentagent.com").rstrip("/")
API = f"{BASE_URL}/api"

SLUGS = [
    "hernia-de-disco-sintomas-causas-e-quando-a-cirurgia-e-necessaria",
    "aneurisma-cerebral-sintomas-fatores-de-risco-e-tratamentos",
    "dor-nas-costas-constante-como-diferenciar-dor-muscular-de-problema-grave",
]


# Articles list
def test_list_articles_returns_three():
    r = requests.get(f"{API}/articles", timeout=30)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 3
    slugs = {a["slug"] for a in data}
    for s in SLUGS:
        assert s in slugs
    # content_html should be excluded from summary
    assert "content_html" not in data[0]
    # ordering by published_at desc -> dor-nas-costas (2026-02-02) first
    assert data[0]["slug"] == "dor-nas-costas-constante-como-diferenciar-dor-muscular-de-problema-grave"


@pytest.mark.parametrize("cat,expected_slug", [
    ("brain", "aneurisma-cerebral-sintomas-fatores-de-risco-e-tratamentos"),
    ("spine", "hernia-de-disco-sintomas-causas-e-quando-a-cirurgia-e-necessaria"),
    ("prevention", "dor-nas-costas-constante-como-diferenciar-dor-muscular-de-problema-grave"),
])
def test_articles_filter_by_category(cat, expected_slug):
    r = requests.get(f"{API}/articles", params={"category": cat}, timeout=30)
    assert r.status_code == 200
    data = r.json()
    assert all(a["category"] == cat for a in data)
    assert any(a["slug"] == expected_slug for a in data)


def test_articles_text_search():
    r = requests.get(f"{API}/articles", params={"q": "aneurisma"}, timeout=30)
    assert r.status_code == 200
    data = r.json()
    assert len(data) >= 1
    assert any("aneurisma" in a["title"].lower() or "aneurisma" in a["excerpt"].lower() for a in data)


# Featured
def test_featured_returns_most_recent():
    r = requests.get(f"{API}/articles/featured", timeout=30)
    assert r.status_code == 200
    data = r.json()
    # Most recent is 2026-02-02
    assert data["slug"] == "dor-nas-costas-constante-como-diferenciar-dor-muscular-de-problema-grave"
    assert data["published_at"] == "2026-02-02"


# Most read
def test_most_read_sorted_by_views():
    r = requests.get(f"{API}/articles/most-read", params={"limit": 5}, timeout=30)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    views = [a.get("views", 0) for a in data]
    assert views == sorted(views, reverse=True)


# Article detail + view counter
def test_article_detail_increments_views():
    slug = SLUGS[0]
    r1 = requests.get(f"{API}/articles/{slug}", timeout=30)
    assert r1.status_code == 200
    d1 = r1.json()
    assert d1["slug"] == slug
    assert "content_html" in d1 and len(d1["content_html"]) > 100
    v1 = d1["views"]

    r2 = requests.get(f"{API}/articles/{slug}", timeout=30)
    assert r2.status_code == 200
    v2 = r2.json()["views"]
    assert v2 == v1 + 1


def test_article_detail_not_found():
    r = requests.get(f"{API}/articles/non-existent-slug-xyz", timeout=30)
    assert r.status_code == 404


# Categories
def test_categories_returns_three():
    r = requests.get(f"{API}/categories", timeout=30)
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 3
    slugs = {c["slug"] for c in data}
    assert slugs == {"brain", "spine", "prevention"}


# Newsletter
def test_newsletter_signup_and_duplicate():
    email = f"test_{uuid.uuid4().hex[:10]}@example.com"
    r = requests.post(f"{API}/newsletter", json={"email": email}, timeout=30)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["email"] == email
    assert "id" in body and "subscribed_at" in body
    assert "_id" not in body

    # duplicate
    r2 = requests.post(f"{API}/newsletter", json={"email": email}, timeout=30)
    assert r2.status_code == 409


def test_newsletter_invalid_email():
    r = requests.post(f"{API}/newsletter", json={"email": "not-an-email"}, timeout=30)
    assert r.status_code == 422
