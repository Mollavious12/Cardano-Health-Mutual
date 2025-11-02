import reflex as rx
from typing import TypedDict
import datetime
import logging
from app.states.state import State
import random
import string


class Claim(TypedDict):
    id: str
    type: str
    amount: float
    status: str
    date_submitted: str
    documents: list[str]


class ClaimsState(State):
    """State for the claims page."""

    claims: list[Claim] = []
    is_loading: bool = False
    is_uploading: bool = False
    uploaded_document_names: list[str] = []

    @rx.event
    async def get_claims(self):
        """Get all claims for the current user from the database."""
        self.is_loading = True
        try:
            user_id = self.clerk_user_id
            if user_id:
                self.claims = await self.db.get_user_claims(user_id)
            else:
                self.claims = []
                yield rx.toast.error("User not authenticated. Please log in.")
        except Exception as e:
            logging.exception(f"Failed to fetch claims: {e}")
            yield rx.toast.error(f"Database error: Could not fetch claims.")
        finally:
            self.is_loading = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of claim documents to Supabase storage."""
        if not files:
            return
        self.is_uploading = True
        try:
            for file in files:
                upload_data = await file.read()
                random_prefix = "".join(
                    random.choices(string.ascii_letters + string.digits, k=8)
                )
                unique_name = f"{random_prefix}_{file.name}"
                upload_dir = rx.get_upload_dir()
                upload_dir.mkdir(parents=True, exist_ok=True)
                file_path = upload_dir / unique_name
                with file_path.open("wb") as f:
                    f.write(upload_data)
                self.uploaded_document_names.append(unique_name)
            yield rx.toast.success(f"Successfully uploaded {len(files)} document(s).")
        except Exception as e:
            logging.exception(f"Document upload failed: {e}")
            yield rx.toast.error("File upload failed. Please try again.")
        finally:
            self.is_uploading = False

    @rx.event
    async def submit_claim(self, form_data: dict):
        """Submit a new claim to the database."""
        self.is_loading = True
        try:
            claim_type = form_data.get("claim_type", "").strip()
            claim_amount_str = form_data.get("claim_amount", "").strip()
            claim_description = form_data.get("claim_description", "").strip()
            if not all([claim_type, claim_amount_str, claim_description]):
                yield rx.toast.error("Please fill all required fields.")
                return
            try:
                amount = float(claim_amount_str)
                if amount <= 0:
                    yield rx.toast.error("Claim amount must be positive.")
                    return
            except ValueError as e:
                logging.exception(f"Invalid amount format: {e}")
                yield rx.toast.error("Invalid amount format.")
                return
            user_id = self.clerk_user_id
            if not user_id:
                yield rx.toast.error("Authentication error. Please log in again.")
                return
            new_claim = await self.db.create_claim(
                user_id=user_id,
                claim_type=claim_type,
                amount=amount,
                description=claim_description,
                documents=self.uploaded_document_names,
            )
            if new_claim and new_claim.get("id"):
                yield rx.toast.success("Claim submitted successfully!")
                self.uploaded_document_names = []
                yield ClaimsState.get_claims
                yield rx.clear_selected_files("upload_claim_docs")
            else:
                yield rx.toast.error("Failed to save claim. Please try again.")
        except Exception as e:
            logging.exception(f"Failed to submit claim: {e}")
            yield rx.toast.error("An unexpected error occurred during submission.")
        finally:
            self.is_loading = False