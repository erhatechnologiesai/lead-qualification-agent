import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestLeadAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_enterprise_qualification(self):
        lead = {
            "lead_id": "LD-9901",
            "company_name": "Apex Global Logistics",
            "employee_count": 1200,
            "annual_revenue_usd": 25000000,
            "industry": "Supply Chain",
            "decision_maker_title": "VP of Technology",
            "current_pain_points": ["Manual document classification", "Slow customer resolution", "Legacy RPA failures"]
        }
        res = self.client.post("/qualify", json=lead)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["classification"], "TIER_1_ENTERPRISE")
        self.assertGreaterEqual(data["score"], 80)
        self.assertEqual(data["crm_payload"]["Sync_Status"], "READY_FOR_CRM_EXPORT")

if __name__ == "__main__":
    unittest.main()
