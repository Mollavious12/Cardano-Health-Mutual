import reflex as rx
from typing import TypedDict


class Transaction(TypedDict):
    date: str
    description: str
    amount: float
    status: str


class HealthPlan(TypedDict):
    name: str
    coverage: str
    contribution: float


class Claim(TypedDict):
    id: str
    type: str
    amount: float
    status: str
    date_submitted: str


class DashboardState(rx.State):
    """State for the user dashboard."""

    sidebar_collapsed: bool = False
    balance: float = 125.5
    transactions: list[Transaction] = [
        {
            "date": "2024-05-20",
            "description": "Monthly Contribution",
            "amount": -25.0,
            "status": "Completed",
        },
        {
            "date": "2024-05-15",
            "description": "Initial Deposit",
            "amount": 150.5,
            "status": "Completed",
        },
    ]
    health_plans: list[HealthPlan] = [
        {
            "name": "Basic Mutual Plan",
            "coverage": "Up to $500 for emergencies",
            "contribution": 25.0,
        },
        {
            "name": "Family Plus Plan",
            "coverage": "Up to $2,000 for family care",
            "contribution": 75.0,
        },
    ]
    claims: list[Claim] = [
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
    user_phone: str = "+1 234 567 890"
    user_address: str = "123 Health St, Wellness City"
    user_role: str = "Individual Member"

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed