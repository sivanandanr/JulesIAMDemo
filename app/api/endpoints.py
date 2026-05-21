from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import schemas
from app.services.core_services import IdentityService, ApplicationService, RoleService

router = APIRouter()

# Identity Endpoints
@router.post("/identities/", response_model=schemas.Identity)
def create_identity(identity: schemas.IdentityCreate, db: Session = Depends(get_db)):
    return IdentityService.create_identity(db=db, identity=identity)

@router.get("/identities/", response_model=List[schemas.Identity])
def read_identities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return IdentityService.get_identities(db, skip=skip, limit=limit)

@router.get("/identities/{identity_id}", response_model=schemas.Identity)
def read_identity(identity_id: int, db: Session = Depends(get_db)):
    db_identity = IdentityService.get_identity(db, identity_id=identity_id)
    if db_identity is None:
        raise HTTPException(status_code=404, detail="Identity not found")
    return db_identity

# Application Endpoints
@router.post("/applications/", response_model=schemas.Application)
def create_application(application: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    return ApplicationService.create_application(db=db, application=application)

@router.post("/entitlements/", response_model=schemas.Entitlement)
def create_entitlement(entitlement: schemas.EntitlementCreate, db: Session = Depends(get_db)):
    return ApplicationService.create_entitlement(db=db, entitlement=entitlement)

# Role Endpoints
@router.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return RoleService.create_role(db=db, role=role)

@router.post("/identities/{identity_id}/roles/{role_id}")
def assign_role(identity_id: int, role_id: int, db: Session = Depends(get_db)):
    IdentityService.assign_role_to_identity(db, identity_id, role_id)
    return {"message": "Role assigned successfully"}
