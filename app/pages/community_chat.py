import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.chat_state import ChatState, Message
import reflex_clerk_api as clerk


def message_bubble(message: Message) -> rx.Component:
    is_self = message["sender"] == clerk.ClerkUser.first_name
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed={message['sender']}",
                class_name="h-8 w-8 rounded-full",
            ),
            rx.el.div(
                rx.el.p(message["sender"], class_name="font-semibold text-sm"),
                rx.el.p(message["text"], class_name="text-sm"),
                class_name=rx.cond(
                    is_self,
                    "bg-violet-500 text-white p-3 rounded-lg max-w-xs",
                    "bg-gray-200 text-gray-900 p-3 rounded-lg max-w-xs",
                ),
            ),
            class_name=rx.cond(
                is_self, "flex items-start gap-3 justify-end", "flex items-start gap-3"
            ),
        ),
        class_name="w-full",
    )


def community_chat() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Community Chat", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Connect with other members of the CareChain community.",
                class_name="text-gray-500 mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(ChatState.messages, message_bubble),
                    class_name="flex-1 overflow-y-auto p-6 space-y-4",
                ),
                rx.el.div(
                    rx.el.form(
                        rx.el.input(
                            name="message",
                            placeholder="Type your message...",
                            class_name="flex-1 rounded-full px-4 py-2 border focus:outline-none focus:ring-2 focus:ring-violet-500",
                        ),
                        rx.el.button(
                            rx.icon("send", class_name="h-5 w-5"),
                            type="submit",
                            class_name="bg-violet-500 text-white rounded-full p-3 hover:bg-violet-600",
                        ),
                        on_submit=ChatState.send_message,
                        reset_on_submit=True,
                        class_name="flex items-center gap-2",
                    ),
                    class_name="p-4 border-t bg-white",
                ),
                class_name="flex flex-col h-[70vh] bg-white border rounded-lg shadow-sm",
            ),
            class_name="h-full flex flex-col",
        )
    )