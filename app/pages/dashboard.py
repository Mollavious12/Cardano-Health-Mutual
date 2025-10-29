import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.dashboard_state import DashboardState


def stat_card(icon: str, title: str, value: rx.Var, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6"), class_name=f"p-3 rounded-full {color}"
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm text-gray-500"),
            rx.el.p(value, class_name="text-2xl font-bold"),
        ),
        class_name="flex items-center gap-4 p-4 bg-white border rounded-lg shadow-sm",
    )


def dashboard() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Welcome Back!", class_name="text-3xl font-bold mb-6"),
            rx.el.div(
                stat_card(
                    "wallet",
                    "My Wallet Balance",
                    f"${DashboardState.balance.to_string()}",
                    "bg-blue-100 text-blue-600",
                ),
                stat_card(
                    "shield-check",
                    "Active Plans",
                    DashboardState.health_plans.length().to_string(),
                    "bg-green-100 text-green-600",
                ),
                stat_card(
                    "file-text",
                    "Pending Claims",
                    DashboardState.claims.length().to_string(),
                    "bg-yellow-100 text-yellow-600",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
        )
    )