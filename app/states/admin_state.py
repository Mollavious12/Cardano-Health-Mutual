import reflex as rx
from typing import TypedDict


class User(TypedDict):
    id: str
    name: str
    email: str
    join_date: str
    status: str


class AdminClaim(TypedDict):
    id: str
    user_name: str
    amount: float
    status: str
    date_submitted: str


class AdminState(rx.State):
    """State for the admin panel."""

    total_users: int = 1250
    pending_claims: int = 1
    active_plans: int = 2
    monthly_growth: int = 15
    user_list: list[User] = [
        {
            "id": "USR-001",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "join_date": "2024-01-15",
            "status": "Active",
        },
        {
            "id": "USR-002",
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "join_date": "2024-02-20",
            "status": "Active",
        },
    ]
    claim_list: list[AdminClaim] = [
        {
            "id": "CLM-002",
            "user_name": "Jane Smith",
            "amount": 50.0,
            "status": "Pending",
            "date_submitted": "2024-05-18",
        },
        {
            "id": "CLM-001",
            "user_name": "John Doe",
            "amount": 250.0,
            "status": "Approved",
            "date_submitted": "2024-04-10",
        },
    ]

    @rx.event
    def approve_claim(self, claim_id: str):
        for i, claim in enumerate(self.claim_list):
            if claim["id"] == claim_id and claim["status"] == "Pending":
                self.claim_list[i]["status"] = "Approved"
                self.pending_claims -= 1
                return

    @rx.event
    def reject_claim(self, claim_id: str):
        for i, claim in enumerate(self.claim_list):
            if claim["id"] == claim_id and claim["status"] == "Pending":
                self.claim_list[i]["status"] = "Rejected"
                self.pending_claims -= 1
                return