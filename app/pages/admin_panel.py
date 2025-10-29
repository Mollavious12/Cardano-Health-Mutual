import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.admin_state import AdminState, User, AdminClaim


def admin_stat_card(icon: str, title: str, value: rx.Var, color: str) -> rx.Component:
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


def user_row(user: User) -> rx.Component:
    return rx.el.tr(
        rx.el.td(user["id"], class_name="px-6 py-4"),
        rx.el.td(user["name"], class_name="px-6 py-4"),
        rx.el.td(user["email"], class_name="px-6 py-4"),
        rx.el.td(user["join_date"], class_name="px-6 py-4"),
        rx.el.td(
            rx.el.span(
                user["status"],
                class_name=rx.cond(
                    user["status"] == "Active",
                    "bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    "bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                ),
            ),
            class_name="px-6 py-4",
        ),
    )


def claim_row_admin(claim: AdminClaim) -> rx.Component:
    return rx.el.tr(
        rx.el.td(claim["id"], class_name="px-6 py-4"),
        rx.el.td(claim["user_name"], class_name="px-6 py-4"),
        rx.el.td(f"${claim['amount']:.2f}", class_name="px-6 py-4"),
        rx.el.td(claim["date_submitted"], class_name="px-6 py-4"),
        rx.el.td(
            rx.el.span(
                claim["status"],
                class_name=rx.match(
                    claim["status"],
                    (
                        "Approved",
                        "bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    ),
                    (
                        "Pending",
                        "bg-yellow-100 text-yellow-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    ),
                    (
                        "Rejected",
                        "bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    ),
                    "bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                ),
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.cond(
                claim["status"] == "Pending",
                rx.el.div(
                    rx.el.button(
                        "Approve",
                        on_click=lambda: AdminState.approve_claim(claim["id"]),
                        class_name="text-green-600 hover:text-green-900 text-sm font-medium",
                    ),
                    rx.el.button(
                        "Reject",
                        on_click=lambda: AdminState.reject_claim(claim["id"]),
                        class_name="text-red-600 hover:text-red-900 text-sm font-medium ml-4",
                    ),
                ),
                rx.el.span("--", class_name="text-gray-400"),
            ),
            class_name="px-6 py-4",
        ),
    )


def admin_panel() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Admin Panel", class_name="text-3xl font-bold mb-6"),
            rx.el.div(
                admin_stat_card(
                    "users",
                    "Total Users",
                    AdminState.total_users,
                    "bg-blue-100 text-blue-600",
                ),
                admin_stat_card(
                    "file-text",
                    "Pending Claims",
                    AdminState.pending_claims,
                    "bg-yellow-100 text-yellow-600",
                ),
                admin_stat_card(
                    "shield-check",
                    "Active Health Plans",
                    AdminState.active_plans,
                    "bg-green-100 text-green-600",
                ),
                admin_stat_card(
                    "trending-up",
                    "Monthly Growth",
                    f"{AdminState.monthly_growth}%",
                    "bg-purple-100 text-purple-600",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.h2(
                    "Pending Claims Management", class_name="text-xl font-semibold mb-4"
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th("Claim ID", class_name="px-6 py-3 text-left"),
                                rx.el.th("User", class_name="px-6 py-3 text-left"),
                                rx.el.th("Amount", class_name="px-6 py-3 text-left"),
                                rx.el.th("Submitted", class_name="px-6 py-3 text-left"),
                                rx.el.th("Status", class_name="px-6 py-3 text-left"),
                                rx.el.th("Action", class_name="px-6 py-3 text-left"),
                            ),
                            class_name="bg-gray-50",
                        ),
                        rx.el.tbody(rx.foreach(AdminState.claim_list, claim_row_admin)),
                        class_name="w-full text-sm text-left text-gray-500",
                    ),
                    class_name="relative overflow-x-auto border rounded-lg",
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm mb-8",
            ),
            rx.el.div(
                rx.el.h2("User Management", class_name="text-xl font-semibold mb-4"),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th("User ID", class_name="px-6 py-3 text-left"),
                                rx.el.th("Name", class_name="px-6 py-3 text-left"),
                                rx.el.th("Email", class_name="px-6 py-3 text-left"),
                                rx.el.th("Join Date", class_name="px-6 py-3 text-left"),
                                rx.el.th("Status", class_name="px-6 py-3 text-left"),
                            ),
                            class_name="bg-gray-50",
                        ),
                        rx.el.tbody(rx.foreach(AdminState.user_list, user_row)),
                        class_name="w-full text-sm text-left text-gray-500",
                    ),
                    class_name="relative overflow-x-auto border rounded-lg",
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm",
            ),
        )
    )