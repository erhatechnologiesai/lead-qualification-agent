from fastapi import FastAPI
from app.config import settings
from app.models import LeadProfile, QualificationOutput
from app.services.rules_engine import score_lead

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/qualify", response_model=QualificationOutput)
def qualify(lead: LeadProfile):
    total, classification, breakdown, crm = score_lead(lead)
    return QualificationOutput(
        lead_id=lead.lead_id,
        score=total,
        classification=classification,
        scoring_breakdown=breakdown,
        crm_payload=crm
    )
