from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Entitlement Schemas
class EntitlementBase(BaseModel):
    name: str
    value: str
    application_id: int

class EntitlementCreate(EntitlementBase):
    pass

class Entitlement(EntitlementBase):
    id: int
    class Config:
        from_attributes = True

# Application Schemas
class ApplicationBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: str

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    entitlements: List[Entitlement] = []
    class Config:
        from_attributes = True

# Role Schemas
class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    entitlement_ids: List[int] = []

class Role(RoleBase):
    id: int
    entitlements: List[Entitlement] = []
    class Config:
        from_attributes = True

# Account Schemas
class AccountBase(BaseModel):
    native_identity: str
    identity_id: int
    application_id: int

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    class Config:
        from_attributes = True

# Identity Schemas
class IdentityBase(BaseModel):
    external_id: str
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool = True

class IdentityCreate(IdentityBase):
    pass

class Identity(IdentityBase):
    id: int
    accounts: List[Account] = []
    roles: List[Role] = []
    class Config:
        from_attributes = True
