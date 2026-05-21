from sqlalchemy.orm import Session
from app.models import models

class GovernanceService:
    @staticmethod
    def launch_certification(db: Session, name: str, certifier_id: int):
        certification = models.AccessCertification(name=name, status="Active")
        db.add(certification)
        db.flush()

        # Simple logic: certify all role assignments
        identities = db.query(models.Identity).all()
        for identity in identities:
            for role in identity.roles:
                item = models.CertificationItem(
                    certification_id=certification.id,
                    identity_id=identity.id,
                    role_id=role.id,
                    decision="Pending",
                    certifier_id=certifier_id
                )
                db.add(item)

        db.commit()
        db.refresh(certification)
        return certification

    @staticmethod
    def make_decision(db: Session, item_id: int, decision: str):
        item = db.query(models.CertificationItem).filter(models.CertificationItem.id == item_id).first()
        if item:
            item.decision = decision
            db.commit()
            db.refresh(item)
        return item
