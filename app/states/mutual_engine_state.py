import reflex as rx
from typing import TypedDict
import datetime


class Contribution(TypedDict):
    date: str
    description: str
    amount: float
    status: str


class FundClaim(TypedDict):
    id: str
    type: str
    amount: float
    status: str
    date_submitted: str


class MutualEngineState(rx.State):
    """State for the Financial Mutual Engine."""

    pool_balance: float = 50000.0
    total_members: int = 1250
    total_contributions: float = 75000.0
    total_claims_paid: float = 25000.0
    mobile_money_provider: str = ""
    contribution_amount: str = ""
    contributions: list[Contribution] = [
        {
            "date": "2024-05-20",
            "description": "Monthly Contribution",
            "amount": -25.0,
            "status": "Completed",
        },
        {
            "date": "2024-04-20",
            "description": "Monthly Contribution",
            "amount": -25.0,
            "status": "Completed",
        },
    ]
    fund_claims: list[FundClaim] = [
        {
            "id": "CLM-001",
            "type": "Emergency Visit",
            "amount": 250.0,
            "status": "Approved",
            "date_submitted": "2024-04-10",
        },
        {
            "id": "CLM-002",
            "type": "Medication",
            "amount": 50.0,
            "status": "Pending",
            "date_submitted": "2024-05-18",
        },
    ]

    @rx.event
    def submit_contribution(self, form_data: dict):
        amount_str = form_data.get("contribution_amount", "0").strip()
        provider = form_data.get("mobile_money_provider", "").strip()
        if not amount_str.isnumeric() or not provider:
            return
        amount = float(amount_str)
        self.pool_balance += amount
        self.total_contributions += amount
        self.contributions.insert(
            0,
            {
                "date": datetime.date.today().strftime("%Y-%m-%d"),
                "description": f"Contribution via {provider}",
                "amount": amount,
                "status": "Completed",
            },
        )
        self.contribution_amount = ""
        self.mobile_money_provider = ""