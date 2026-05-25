import pytest
from app import app, PROJECTS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_homepage_renders_all_projects(client):
    """All 5 project titles must appear on the homepage."""
    r = client.get("/")
    assert r.status_code == 200
    html = r.data.decode()
    for project in PROJECTS:
        assert project["title"] in html, f"Missing project: {project['title']}"


def test_contact_post_redirects_to_success(client):
    """Submitting the contact form must redirect to /?sent=1."""
    r = client.post("/contact", data={
        "name": "Test User",
        "email": "test@example.com",
        "message": "Hello",
    })
    assert r.status_code == 302
    assert "sent=1" in r.headers["Location"]
