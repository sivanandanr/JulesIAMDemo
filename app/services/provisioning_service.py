from sqlalchemy.orm import Session
from app.models import models

class ProvisioningService:
    """
    Simulates pushing changes from IAM to target systems.
    """
    @staticmethod
    def provision_account(db: Session, identity_id: int, application_id: int):
        identity = db.query(models.Identity).filter(models.Identity.id == identity_id).first()
        application = db.query(models.Application).filter(models.Application.id == application_id).first()

        if not identity or not application:
            return False

        # Check if account already exists
        existing_account = db.query(models.Account).filter(
            models.Account.identity_id == identity_id,
            models.Account.application_id == application_id
        ).first()

        if not existing_account:
            # In a real system, this would call an API/Connector
            print(f"DEBUG: Provisioning account for {identity.username} on {application.name}")
            new_account = models.Account(
                native_identity=identity.username, # simplified
                identity_id=identity_id,
                application_id=application_id
            )
            db.add(new_account)
            db.commit()
            return True
        return False
