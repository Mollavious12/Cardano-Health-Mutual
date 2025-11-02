import reflex as rx
from typing import TypedDict
import datetime
import reflex_clerk_api as clerk
from app.states.state import State
import logging


class Message(TypedDict):
    sender: str
    text: str
    timestamp: str


class ChatState(State):
    """State for the community chat."""

    messages: list[Message] = []
    is_loading: bool = False

    @rx.event(background=True)
    async def get_messages(self):
        """Get recent chat messages from the database."""
        async with self:
            self.is_loading = True
        try:
            messages_from_db = await self.db.get_messages(limit=100)
            async with self:
                self.messages = messages_from_db
        except Exception as e:
            logging.exception(f"Failed to fetch chat messages: {e}")
            yield rx.toast.error("Could not load chat history.")
        finally:
            async with self:
                self.is_loading = False

    @rx.event(background=True)
    async def send_message(self, form_data: dict):
        """Save a new message and update the chat."""
        message_text = form_data.get("message", "").strip()
        if not message_text:
            return
        user_id = self.clerk_user_id
        sender_name = str(clerk.ClerkUser.first_name)
        if not sender_name or sender_name == "None":
            sender_name = "Anonymous"
        try:
            new_message = await self.db.save_message(
                user_id=user_id, user_name=sender_name, message_text=message_text
            )
            if new_message:
                async with self:
                    self.messages.append(new_message)
            else:
                yield rx.toast.error("Failed to send message.")
        except Exception as e:
            logging.exception(f"Failed to send message: {e}")
            yield rx.toast.error("An error occurred while sending your message.")