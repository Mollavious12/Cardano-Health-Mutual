import reflex as rx
from typing import TypedDict
import datetime
import reflex_clerk_api as clerk


class Message(TypedDict):
    sender: str
    text: str
    timestamp: str


class ChatState(rx.State):
    """State for the community chat."""

    messages: list[Message] = [
        {
            "sender": "Admin",
            "text": "Welcome to the CareChain community chat! Feel free to ask questions and share your experiences.",
            "timestamp": str(datetime.datetime.now()),
        },
        {
            "sender": "Jane Doe",
            "text": "Hi everyone! Glad to be here. How does the claim process work?",
            "timestamp": str(datetime.datetime.now()),
        },
    ]

    @rx.event
    def send_message(self, form_data: dict):
        message_text = form_data.get("message", "").strip()
        if not message_text:
            return
        sender_name = str(clerk.ClerkUser.first_name)
        if not sender_name or sender_name == "None":
            sender_name = "Anonymous"
        self.messages.append(
            {
                "sender": sender_name,
                "text": message_text,
                "timestamp": str(datetime.datetime.now()),
            }
        )