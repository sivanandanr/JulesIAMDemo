from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

class IdentityService:
    @staticmethod
    def get_identity(db: Session, identity_id: int):
        return db.query(models.Identity).filter(models.Identity.id == identity_id).first()

    @staticmethod
    def get_identities(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Identity).offset(skip).limit(limit).all()

    @staticmethod
    def create_identity(db: Session, identity: schemas.IdentityCreate):
        db_identity = models.Identity(**identity.model_dump())
        db.add(db_identity)
        db.commit()
        db.refresh(db_identity)
        return db_identity

class ApplicationService:
    @staticmethod
    def create_application(db: Session, application: schemas.ApplicationCreate):
        db_application = models.Application(**application.model_dump())
        db.add(db_application)
        db.commit()
        db.refresh(db_application)
        return db_application

    @staticmethod
    def create_entitlement(db: Session, entitlement: schemas.EntitlementCreate):
        db_entitlement = models.Entitlement(**entitlement.model_dump())
        db.add(db_entitlement)
        db.commit()
        db.refresh(db_entitlement)
        return db_entitlement

class RoleService:
    @staticmethod
    def create_role(db: Session, role: schemas.RoleCreate):
        db_role = models.Role(name=role.name, description=role.description)
        if role.entitlement_ids:
            entitlements = db.query(models.Entitlement).filter(models.Entitlement.id.in_(role.entitlement_ids)).all()
            db_role.entitlements = entitlements
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role

    @staticmethod
    def assign_role_to_identity(db: Session, identity_id: int, role_id: int):
        identity = db.query(models.Identity).filter(models.Identity.id == identity_id).first()
        role = db.query(models.Role).filter(models.Role.id == role_id).first()
        if identity and role:
            identity.roles.append(role)
            db.commit()
        return identity
