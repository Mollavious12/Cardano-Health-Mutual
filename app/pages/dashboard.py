import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.dashboard_state import DashboardState, Transaction
import reflex_clerk_api as clerk


def stat_card(icon: str, title: str, value: rx.Var, color_class: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(rx.icon(icon, class_name="h-8 w-8"), class_name="p-3 rounded-lg"),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium"),
            rx.el.p(value, class_name="text-3xl font-bold"),
        ),
        class_name=f"flex items-center gap-4 p-6 rounded-2xl text-white {color_class}",
    )


def stat_card_skeleton() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="h-14 w-14 bg-gray-300 rounded-lg"),
        rx.el.div(
            rx.el.div(class_name="h-4 w-24 bg-gray-300 rounded"),
            rx.el.div(class_name="h-8 w-32 bg-gray-300 rounded mt-2"),
        ),
        class_name="flex items-center gap-4 p-6 rounded-2xl bg-gray-200 animate-pulse",
    )


def quick_action_button(icon: str, text: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5 mr-2"),
        text,
        href=href,
        class_name="flex items-center justify-center px-4 py-2 bg-white border border-gray-200 rounded-lg shadow-sm hover:bg-gray-50 transition-colors font-medium text-sm",
    )


def transaction_row(transaction: Transaction) -> rx.Component:
    is_credit = transaction["amount"] >= 0
    return rx.el.tr(
        rx.el.td(transaction["date"], class_name="px-4 py-3"),
        rx.el.td(transaction["description"], class_name="px-4 py-3"),
        rx.el.td(
            f"${abs(transaction['amount']):.2f}",
            class_name=rx.cond(
                is_credit, "text-green-600 font-semibold", "text-red-600 font-semibold"
            ),
        ),
        rx.el.td(
            rx.el.span(
                transaction["status"],
                class_name="text-xs font-medium px-2.5 py-1 rounded-full bg-green-100 text-green-800",
            )
        ),
    )


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            f"Welcome Back, {clerk.ClerkUser.first_name}!",
            class_name="text-3xl font-bold mb-6",
        ),
        rx.cond(
            DashboardState.is_loading,
            rx.el.div(
                stat_card_skeleton(),
                stat_card_skeleton(),
                stat_card_skeleton(),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
            rx.el.div(
                stat_card(
                    "wallet",
                    "My Wallet Balance",
                    f"${DashboardState.balance:.2f}",
                    "bg-gradient-to-br from-blue-500 to-blue-600",
                ),
                stat_card(
                    "shield-check",
                    "Active Plans",
                    DashboardState.health_plans.length().to_string(),
                    "bg-gradient-to-br from-green-500 to-green-600",
                ),
                stat_card(
                    "file-text",
                    "Pending Claims",
                    DashboardState.pending_claims_count.to_string(),
                    "bg-gradient-to-br from-yellow-500 to-yellow-600",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
        ),
        rx.el.div(
            quick_action_button("circle_plus", "Add Funds", "/wallet"),
            quick_action_button("file-plus-2", "Submit Claim", "/claims"),
            quick_action_button("shield", "View Coverage", "/coverage"),
            class_name="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8",
        ),
        rx.el.div(
            rx.el.h2("Recent Activity", class_name="text-xl font-semibold mb-4"),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Date", class_name="text-left font-semibold px-4 py-2"
                            ),
                            rx.el.th(
                                "Description",
                                class_name="text-left font-semibold px-4 py-2",
                            ),
                            rx.el.th(
                                "Amount", class_name="text-left font-semibold px-4 py-2"
                            ),
                            rx.el.th(
                                "Status", class_name="text-left font-semibold px-4 py-2"
                            ),
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(DashboardState.recent_transactions, transaction_row)
                    ),
                    class_name="w-full text-sm",
                ),
                class_name="relative overflow-x-auto border rounded-lg bg-white",
            ),
            class_name="bg-white p-6 rounded-lg border shadow-sm",
        ),
    )


def dashboard() -> rx.Component:
    return dashboard_layout(
        rx.el.div(dashboard_content(), on_mount=DashboardState.load_dashboard_data)
    )