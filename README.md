# Mini-IAM: A SailPoint-inspired Identity and Access Management Application

This project aims to implement the core functionalities of an Identity and Access Management (IAM) system, inspired by SailPoint IdentityIQ.

## Core Features (Roadmap)

1.  **Identity Governance Platform**: Central repository for identity data, roles, and entitlements.
2.  **Identity Lifecycle Management**: Automated provisioning, de-provisioning, and access requests.
3.  **Compliance Manager**: Access certifications and Separation of Duties (SoD) policies.
4.  **Connectors**: Framework to integrate with target applications (Active Directory, LDAP, SaaS apps, etc.).

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite (SQLAlchemy ORM)
- **Testing**: Pytest

## Project Structure

- `app/api/`: REST API endpoints.
- `app/models/`: Database models.
- `app/schemas/`: Pydantic models for validation.
- `app/services/`: Business logic (Provisioning, Aggregation, Governance).
- `app/core/`: Configuration and security.
