import reflex as rx
import os
import reflex_clerk_api as clerk
from app.services.database import MongoDBService


class State(rx.State):
    """The base state for the app."""

    members: int = 0
    funds_raised: float = 0.0
    lives_supported: int = 0
    _db: MongoDBService | None = None

    @rx.event
    async def load_platform_stats(self):
        stats = await self.db.get_platform_statistics()
        self.members = stats.get("total_users", 0)
        self.funds_raised = stats.get("pool_balance", 0.0)
        self.lives_supported = stats.get("total_claims_paid", 0)

    @rx.var
    def db(self) -> MongoDBService:
        """Get the database service."""
        if self._db is None:
            self._db = MongoDBService()
        return self._db

    @rx.var
    def clerk_user_id(self) -> str:
        return str(clerk.ClerkState.user_id)

    @rx.var
    def formatted_members(self) -> str:
        return f"{self.members:,}"

    @rx.var
    def formatted_funds(self) -> str:
        return f"${self.funds_raised:,.2f}"

    @rx.var
    def formatted_lives(self) -> str:
        return f"{self.lives_supported:,}"