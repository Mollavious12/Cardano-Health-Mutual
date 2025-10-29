import reflex as rx
from app.components.dashboard_layout import dashboard_layout
import reflex_clerk_api as clerk


def profile() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("User Profile", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Manage your personal information and settings.",
                class_name="text-gray-500 mb-8",
            ),
            rx.el.div(
                clerk.user_profile(),
                class_name="bg-white p-8 rounded-lg border shadow-sm max-w-4xl mx-auto",
            ),
        )
    )