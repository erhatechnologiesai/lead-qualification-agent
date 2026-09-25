def score_lead(lead):
    breakdown = {}
    
    # 1. Company Size (Max 30)
    if lead.employee_count >= 500:
        breakdown["company_size"] = 30
    elif lead.employee_count >= 50:
        breakdown["company_size"] = 20
    else:
        breakdown["company_size"] = 10

    # 2. Revenue (Max 30)
    if lead.annual_revenue_usd >= 10_000_000:
        breakdown["revenue"] = 30
    elif lead.annual_revenue_usd >= 1_000_000:
        breakdown["revenue"] = 20
    else:
        breakdown["revenue"] = 10

    # 3. Decision Maker Authority (Max 25)
    title = lead.decision_maker_title.lower()
    if any(k in title for k in ["cto", "ceo", "vp", "director", "head of", "cio"]):
        breakdown["authority"] = 25
    else:
        breakdown["authority"] = 10

    # 4. Pain points clarity (Max 15)
    breakdown["need_urgency"] = min(15, len(lead.current_pain_points) * 5)
    
    total = sum(breakdown.values())
    
    if total >= 80:
        classification = "TIER_1_ENTERPRISE"
        owner = "Enterprise Solutions Director"
    elif total >= 55:
        classification = "TIER_2_MID_MARKET"
        owner = "Senior Account Executive"
    else:
        classification = "TIER_3_SMB"
        owner = "Inside Sales Specialist"

    crm_payload = {
        "HubSpot_Company": lead.company_name,
        "HubSpot_Score": str(total),
        "HubSpot_Tier": classification,
        "Assigned_Owner": owner,
        "Sync_Status": "READY_FOR_CRM_EXPORT"
    }

    return total, classification, breakdown, crm_payload
