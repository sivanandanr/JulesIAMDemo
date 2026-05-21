from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Many-to-many relationship for Roles and Entitlements
role_entitlement = Table(
    "role_entitlement",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("entitlement_id", Integer, ForeignKey("entitlements.id"), primary_key=True),
)

# Many-to-many relationship for Identities and Roles
identity_role = Table(
    "identity_role",
    Base.metadata,
    Column("identity_id", Integer, ForeignKey("identities.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
)

class Identity(Base):
    __tablename__ = "identities"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)

    accounts = relationship("Account", back_populates="identity")
    roles = relationship("Role", secondary=identity_role, back_populates="identities")

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    type = Column(String) # e.g., "Active Directory", "LDAP", "SaaS"

    entitlements = relationship("Entitlement", back_populates="application")
    accounts = relationship("Account", back_populates="application")

class Entitlement(Base):
    __tablename__ = "entitlements"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(String)
    application_id = Column(Integer, ForeignKey("applications.id"))

    application = relationship("Application", back_populates="entitlements")
    roles = relationship("Role", secondary=role_entitlement, back_populates="entitlements")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    entitlements = relationship("Entitlement", secondary=role_entitlement, back_populates="roles")
    identities = relationship("Identity", secondary=identity_role, back_populates="roles")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    native_identity = Column(String, index=True)
    identity_id = Column(Integer, ForeignKey("identities.id"))
    application_id = Column(Integer, ForeignKey("applications.id"))

    identity = relationship("Identity", back_populates="accounts")
    application = relationship("Application", back_populates="accounts")

class AccessCertification(Base):
    __tablename__ = "access_certifications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String) # e.g., "Active", "Completed"

    items = relationship("CertificationItem", back_populates="certification")

class CertificationItem(Base):
    __tablename__ = "certification_items"
    id = Column(Integer, primary_key=True, index=True)
    certification_id = Column(Integer, ForeignKey("access_certifications.id"))
    identity_id = Column(Integer, ForeignKey("identities.id"))
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    entitlement_id = Column(Integer, ForeignKey("entitlements.id"), nullable=True)
    decision = Column(String) # "Approve", "Revoke", "Pending"
    certifier_id = Column(Integer, ForeignKey("identities.id"))

    certification = relationship("AccessCertification", back_populates="items")
    identity = relationship("Identity", foreign_keys=[identity_id])
    certifier = relationship("Identity", foreign_keys=[certifier_id])
