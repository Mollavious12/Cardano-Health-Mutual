import reflex as rx
import os
import logging
from typing import Optional
from datetime import datetime


class MongoDBService:
    """Service for managing all database operations with MongoDB."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("MongoDB service initialized with mock data")

    def _to_json(self, data):
        """Recursively convert MongoDB documents to JSON-serializable dicts."""
        if data is None:
            return None
        if isinstance(data, list):
            return [self._to_json(item) for item in data]
        if isinstance(data, dict) and "_id" in data:
            data["id"] = str(data.pop("_id"))
        return data

    async def get_or_create_user(
        self, user_id: str, full_name: str, email: str
    ) -> dict | None:
        """Get an existing user or create a new one if not found."""
        try:
            return {
                "id": user_id,
                "clerk_id": user_id,
                "full_name": full_name,
                "email": email,
                "balance": 125.5,
                "created_at": datetime.now(),
            }
        except Exception as e:
            self.logger.exception(f"Error in get_or_create_user: {e}")
            return None

    async def get_user_balance(self, user_id: str) -> float:
        """Get a user's current balance."""
        try:
            return 125.5
        except Exception as e:
            self.logger.exception(f"Error getting user balance: {e}")
            return 0.0

    async def update_user_balance(
        self, user_id: str, amount: float, operation: str = "add"
    ) -> bool:
        """Update a user's balance (add or subtract)."""
        try:
            return True
        except Exception as e:
            self.logger.exception(f"Error updating user balance: {e}")
            return False

    async def create_transaction(
        self,
        user_id: str,
        transaction_type: str,
        amount: float,
        description: str,
        status: str = "Completed",
    ) -> dict | None:
        """Create a new transaction record."""
        try:
            transaction = {
                "id": f"txn_{datetime.now().timestamp()}",
                "user_id": user_id,
                "type": transaction_type,
                "amount": amount,
                "description": description,
                "status": status,
                "date": datetime.now().strftime("%Y-%m-%d"),
            }
            return transaction
        except Exception as e:
            self.logger.exception(f"Error creating transaction: {e}")
            return None

    async def get_user_transactions(self, user_id: str, limit: int = 50) -> list[dict]:
        """Get a user's transaction history."""
        try:
            return [
                {
                    "id": "txn_001",
                    "date": "2024-05-20",
                    "description": "Monthly Contribution",
                    "amount": -25.0,
                    "status": "Completed",
                },
                {
                    "id": "txn_002",
                    "date": "2024-05-15",
                    "description": "Initial Deposit",
                    "amount": 150.5,
                    "status": "Completed",
                },
            ]
        except Exception as e:
            self.logger.exception(f"Error getting user transactions: {e}")
            return []

    async def create_claim(
        self,
        user_id: str,
        claim_type: str,
        amount: float,
        description: str,
        documents: list[str] | None = None,
    ) -> dict | None:
        """Create a new claim."""
        try:
            claim = {
                "id": f"clm_{datetime.now().timestamp()}",
                "user_id": user_id,
                "type": claim_type,
                "amount": amount,
                "description": description,
                "status": "Pending",
                "documents": documents or [],
                "date_submitted": datetime.now().strftime("%Y-%m-%d"),
            }
            return claim
        except Exception as e:
            self.logger.exception(f"Error creating claim: {e}")
            return None

    async def get_user_claims(self, user_id: str) -> list[dict]:
        """Get all claims for a user."""
        try:
            return [
                {
                    "id": "CLM-001",
                    "type": "Emergency Visit",
                    "amount": 250.0,
                    "status": "Approved",
                    "date_submitted": "2024-04-10",
                    "documents": [],
                },
                {
                    "id": "CLM-002",
                    "type": "Medication",
                    "amount": 50.0,
                    "status": "Pending",
                    "date_submitted": "2024-05-18",
                    "documents": [],
                },
            ]
        except Exception as e:
            self.logger.exception(f"Error getting claims for user: {e}")
            return []

    async def update_claim_status(
        self, claim_id: str, status: str, admin_notes: str | None = None
    ) -> bool:
        """Update claim status (Pending/Approved/Rejected)."""
        try:
            return True
        except Exception as e:
            self.logger.exception(f"Error updating claim status: {e}")
            return False

    async def get_all_claims_for_admin(
        self, status_filter: Optional[str] = None
    ) -> list[dict]:
        """Get all claims for admin panel, joining with user data."""
        try:
            return [
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
        except Exception as e:
            self.logger.exception(f"Error getting admin claims: {e}")
            return []

    async def create_contribution(
        self, user_id: str, amount: float, provider: str
    ) -> dict | None:
        """Record a new contribution to the mutual pool."""
        try:
            contribution = {
                "id": f"contrib_{datetime.now().timestamp()}",
                "user_id": user_id,
                "amount": amount,
                "provider": provider,
                "status": "Completed",
                "date": datetime.now().strftime("%Y-%m-%d"),
            }
            return contribution
        except Exception as e:
            self.logger.exception(f"Error creating contribution: {e}")
            return None

    async def get_contributions(self, user_id: str) -> list[dict]:
        """Get contribution history for a user."""
        try:
            return [
                {
                    "id": "contrib_001",
                    "date": "2024-05-20",
                    "description": "Monthly Contribution",
                    "amount": -25.0,
                    "status": "Completed",
                },
                {
                    "id": "contrib_002",
                    "date": "2024-04-20",
                    "description": "Monthly Contribution",
                    "amount": -25.0,
                    "status": "Completed",
                },
            ]
        except Exception as e:
            self.logger.exception(f"Error getting contributions: {e}")
            return []

    async def get_platform_statistics(self) -> dict:
        """Get overall platform statistics."""
        try:
            return {
                "total_users": 1250,
                "pool_balance": 50000.0,
                "total_contributions": 75000.0,
                "total_claims_paid": 25000.0,
                "pending_claims": 1,
                "active_plans": 2,
            }
        except Exception as e:
            self.logger.exception(f"Error getting platform statistics: {e}")
            return {
                "total_users": 1250,
                "pool_balance": 50000.0,
                "total_contributions": 75000.0,
                "total_claims_paid": 25000.0,
                "pending_claims": 1,
                "active_plans": 2,
            }

    async def save_message(
        self, user_id: str, user_name: str, message_text: str
    ) -> dict | None:
        """Save a chat message to the database."""
        try:
            message = {
                "id": f"msg_{datetime.now().timestamp()}",
                "user_id": user_id,
                "sender": user_name,
                "text": message_text,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            return message
        except Exception as e:
            self.logger.exception(f"Error saving message: {e}")
            return None

    async def get_messages(self, limit: int = 100) -> list[dict]:
        """Get recent chat messages."""
        try:
            return [
                {
                    "sender": "Admin",
                    "text": "Welcome to the CareChain community chat! Feel free to ask questions and share your experiences.",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                },
                {
                    "sender": "Jane Doe",
                    "text": "Hi everyone! Glad to be here. How does the claim process work?",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                },
            ]
        except Exception as e:
            self.logger.exception(f"Error getting messages: {e}")
            return []