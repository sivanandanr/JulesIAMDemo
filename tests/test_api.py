import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_api.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Mini-IAM API"}

def test_create_identity_api():
    response = client.post(
        "/api/v1/identities/",
        json={
            "external_id": "EXT456",
            "username": "asmith",
            "email": "asmith@example.com",
            "first_name": "Alice",
            "last_name": "Smith"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "asmith"
    assert "id" in data

def test_get_identities_api():
    client.post(
        "/api/v1/identities/",
        json={
            "external_id": "EXT456",
            "username": "asmith",
            "email": "asmith@example.com",
            "first_name": "Alice",
            "last_name": "Smith"
        }
    )
    response = client.get("/api/v1/identities/")
    assert response.status_code == 200
    assert len(response.json()) == 1
