from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

class AggregationService:
    """
    Simulates fetching data from target systems and updating the IAM repository.
    """
    @staticmethod
    def aggregate_accounts(db: Session, application_id: int, external_accounts: list):
        """
        external_accounts is a list of dicts: [{"native_identity": "jdoe", "email": "john.doe@example.com"}]
        """
        application = db.query(models.Application).filter(models.Application.id == application_id).first()
        if not application:
            return None

        results = {"created": 0, "linked": 0}
        for ext_acc in external_accounts:
            # 1. Look for existing identity by email or username
            identity = db.query(models.Identity).filter(
                (models.Identity.email == ext_acc["email"]) |
                (models.Identity.username == ext_acc["native_identity"])
            ).first()

            if identity:
                # 2. Check if account already exists
                existing_account = db.query(models.Account).filter(
                    models.Account.native_identity == ext_acc["native_identity"],
                    models.Account.application_id == application_id
                ).first()

                if not existing_account:
                    new_account = models.Account(
                        native_identity=ext_acc["native_identity"],
                        identity_id=identity.id,
                        application_id=application_id
                    )
                    db.add(new_account)
                    results["linked"] += 1

        db.commit()
        return results
