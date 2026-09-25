from pydantic import BaseModel
from typing import List, Dict, Optional

class LeadProfile(BaseModel):
    lead_id: str
    company_name: str
    employee_count: int
    annual_revenue_usd: int
    industry: str
    decision_maker_title: str
    current_pain_points: List[str]

class QualificationOutput(BaseModel):
    lead_id: str
    score: int
    classification: str # TIER_1_ENTERPRISE, TIER_2_MID_MARKET, TIER_3_SMB, DISQUALIFIED
    scoring_breakdown: Dict[str, int]
    crm_payload: Dict[str, str]
