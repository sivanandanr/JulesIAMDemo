import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from app.services.core_services import IdentityService, ApplicationService, RoleService
from app.services.aggregation_service import AggregationService
from app.schemas import schemas

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_identity(db):
    identity_data = schemas.IdentityCreate(
        external_id="EXT123",
        username="jdoe",
        email="jdoe@example.com",
        first_name="John",
        last_name="Doe"
    )
    identity = IdentityService.create_identity(db, identity_data)
    assert identity.username == "jdoe"
    assert identity.id is not None

def test_aggregation(db):
    # Setup application
    app_data = schemas.ApplicationCreate(name="AD", type="Active Directory")
    application = ApplicationService.create_application(db, app_data)

    # Setup identity
    identity_data = schemas.IdentityCreate(
        external_id="EXT123",
        username="jdoe",
        email="jdoe@example.com",
        first_name="John",
        last_name="Doe"
    )
    IdentityService.create_identity(db, identity_data)

    # Aggregate
    external_accounts = [{"native_identity": "jdoe", "email": "jdoe@example.com"}]
    results = AggregationService.aggregate_accounts(db, application.id, external_accounts)

    assert results["linked"] == 1

    # Verify account creation
    identity = IdentityService.get_identity(db, 1)
    assert len(identity.accounts) == 1
    assert identity.accounts[0].application_id == application.id
