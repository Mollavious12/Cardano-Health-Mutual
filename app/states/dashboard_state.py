import reflex as rx
from typing import TypedDict
from app.states.state import State
import logging


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


class DashboardState(State):
    """State for the user dashboard."""

    sidebar_collapsed: bool = False
    is_loading: bool = True
    balance: float = 0.0
    transactions: list[Transaction] = []
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
    claims: list[Claim] = []
    user_phone: str = "+1 234 567 890"
    user_address: str = "123 Health St, Wellness City"
    user_role: str = "Individual Member"

    @rx.var
    def pending_claims_count(self) -> int:
        return len([c for c in self.claims if c["status"] == "Pending"])

    @rx.var
    def recent_transactions(self) -> list[Transaction]:
        return self.transactions[:5]

    @rx.event
    async def load_dashboard_data(self):
        """Load all necessary data for the dashboard from the database."""
        self.is_loading = True
        try:
            user_id = self.clerk_user_id
            if not user_id:
                logging.warning("Dashboard loading skipped: User not authenticated.")
                yield rx.toast.error("Authentication error. Please log in.")
                return
            self.balance = await self.db.get_user_balance(user_id)
            self.transactions = await self.db.get_user_transactions(user_id, limit=10)
            self.claims = await self.db.get_user_claims(user_id)
            yield rx.toast.success("Dashboard data loaded.")
        except Exception as e:
            logging.exception(f"Error loading dashboard data: {e}")
            yield rx.toast.error("Failed to load dashboard data. Please refresh.")
        finally:
            self.is_loading = False

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed