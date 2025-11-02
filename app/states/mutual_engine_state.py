import reflex as rx
from typing import TypedDict, Literal
import datetime
import time
import logging
from app.states.state import State


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


PaymentStatus = Literal["idle", "processing", "success", "failed"]


class MutualEngineState(State):
    """State for the Financial Mutual Engine."""

    pool_balance: float = 50000.0
    total_members: int = 1250
    total_contributions: float = 75000.0
    total_claims_paid: float = 25000.0
    mobile_money_provider: str = ""
    contribution_amount: str = ""
    contributions: list[Contribution] = []
    fund_claims: list[FundClaim] = []
    payment_status: PaymentStatus = "idle"
    last_transaction_id: str | None = None

    @rx.event(background=True)
    async def load_mutual_engine_data(self):
        """Load data for the mutual engine from the database."""
        async with self:
            self.payment_status = "processing"
        try:
            stats = await self.db.get_platform_statistics()
            async with self:
                self.pool_balance = stats.get("pool_balance", 0.0)
                self.total_members = stats.get("total_users", 0)
                self.total_contributions = stats.get("total_contributions", 0.0)
                self.total_claims_paid = stats.get("total_claims_paid", 0.0)
            user_id = self.clerk_user_id
            if user_id:
                contribs = await self.db.get_contributions(user_id)
                async with self:
                    self.contributions = contribs
            yield rx.toast.info("Mutual engine data loaded.")
        except Exception as e:
            logging.exception(f"Error loading mutual engine data: {e}")
            yield rx.toast.error("Failed to load data. Please refresh.")
        finally:
            async with self:
                self.payment_status = "idle"

    def _validate_contribution(self, amount_str: str, provider: str) -> float | None:
        if not provider:
            yield rx.toast.error("Please select a mobile money provider.")
            return None
        try:
            amount = float(amount_str)
            if not 5 <= amount <= 500:
                yield rx.toast.error("Contribution must be between $5 and $500.")
                return None
            return amount
        except (ValueError, TypeError) as e:
            logging.exception(f"Invalid amount format: {e}")
            yield rx.toast.error("Invalid amount entered.")
            return None

    @rx.event(background=True)
    async def process_contribution(self, form_data: dict):
        """Process a new contribution with validation and simulated delay."""
        async with self:
            self.payment_status = "processing"
            self.last_transaction_id = None
        amount_str = form_data.get("contribution_amount", "").strip()
        provider = form_data.get("mobile_money_provider", "").strip()
        amount = self._validate_contribution(amount_str, provider)
        if amount is None:
            async with self:
                self.payment_status = "failed"
            yield
            return
        try:
            yield rx.toast.info(
                f"Processing ${amount:.2f} contribution via {provider}..."
            )
            time.sleep(2)
            user_id = self.clerk_user_id
            if not user_id:
                yield rx.toast.error("Authentication failed. Please log in.")
                async with self:
                    self.payment_status = "failed"
                return
            new_contribution = await self.db.create_contribution(
                user_id=user_id, amount=amount, provider=provider
            )
            if not new_contribution:
                raise Exception("Database operation failed.")
            async with self:
                self.pool_balance += amount
                self.total_contributions += amount
                self.contributions.insert(0, new_contribution)
                self.payment_status = "success"
                self.last_transaction_id = new_contribution.get("id")
                self.contribution_amount = ""
                self.mobile_money_provider = ""
            yield rx.toast.success("Contribution successful!")
        except Exception as e:
            logging.exception(f"Contribution failed: {e}")
            async with self:
                self.payment_status = "failed"
            yield rx.toast.error("Payment failed. Please try again.")