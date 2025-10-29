import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.mutual_engine_state import MutualEngineState, Contribution, FundClaim


def stat_card(icon: str, title: str, value: rx.Var, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8"), class_name=f"p-4 rounded-lg {color}"
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm text-gray-500"),
            rx.el.p(value, class_name="text-3xl font-bold"),
        ),
        class_name="flex items-center gap-6 p-6 bg-white border rounded-lg shadow-sm",
    )


def contribution_row(contribution: Contribution) -> rx.Component:
    is_credit = contribution["amount"] >= 0
    return rx.el.tr(
        rx.el.td(contribution["date"], class_name="px-6 py-4"),
        rx.el.td(contribution["description"], class_name="px-6 py-4"),
        rx.el.td(
            f"${rx.cond(is_credit, '', '-')}{abs(contribution['amount']):.2f}",
            class_name=rx.cond(is_credit, "text-green-600", "text-red-600"),
        ),
        rx.el.td(
            rx.el.span(
                contribution["status"],
                class_name="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
            ),
            class_name="px-6 py-4",
        ),
    )


def mutual_engine() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Financial Mutual Engine", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Contribute to the community pool and track fund health in real-time.",
                class_name="text-gray-500 mb-8",
            ),
            rx.el.div(
                stat_card(
                    "landmark",
                    "Pool Balance",
                    f"${MutualEngineState.pool_balance:,.2f}",
                    "bg-blue-100 text-blue-600",
                ),
                stat_card(
                    "users",
                    "Total Members",
                    MutualEngineState.total_members,
                    "bg-green-100 text-green-600",
                ),
                stat_card(
                    "trending-up",
                    "Contributions",
                    f"${MutualEngineState.total_contributions:,.2f}",
                    "bg-purple-100 text-purple-600",
                ),
                stat_card(
                    "trending-down",
                    "Claims Paid",
                    f"${MutualEngineState.total_claims_paid:,.2f}",
                    "bg-yellow-100 text-yellow-600",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.h2(
                    "Make a Contribution", class_name="text-xl font-semibold mb-4"
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Mobile Money Provider",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.select(
                                rx.el.option(
                                    "Select Provider", value="", disabled=True
                                ),
                                rx.el.option(
                                    "MTN Mobile Money", value="MTN Mobile Money"
                                ),
                                rx.el.option("Airtel Money", value="Airtel Money"),
                                rx.el.option("M-Pesa", value="M-Pesa"),
                                name="mobile_money_provider",
                                class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                                default_value=MutualEngineState.mobile_money_provider,
                            ),
                            class_name="flex-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Amount (USD)",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.input(
                                name="contribution_amount",
                                type="number",
                                placeholder="e.g., 25",
                                class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                                default_value=MutualEngineState.contribution_amount,
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex flex-col md:flex-row gap-4 mb-4",
                    ),
                    rx.el.button(
                        "Contribute Now",
                        type="submit",
                        class_name="bg-violet-500 text-white px-6 py-2 rounded-md font-semibold hover:bg-violet-600 w-full md:w-auto",
                    ),
                    on_submit=MutualEngineState.submit_contribution,
                    reset_on_submit=True,
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm mb-8",
            ),
            rx.el.div(
                rx.el.h2(
                    "Fund Transaction History", class_name="text-xl font-semibold mb-4"
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th("Date", class_name="px-6 py-3 text-left"),
                                rx.el.th(
                                    "Description", class_name="px-6 py-3 text-left"
                                ),
                                rx.el.th("Amount", class_name="px-6 py-3 text-left"),
                                rx.el.th("Status", class_name="px-6 py-3 text-left"),
                            ),
                            class_name="bg-gray-50",
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                MutualEngineState.contributions, contribution_row
                            )
                        ),
                        class_name="w-full text-sm text-left text-gray-500",
                    ),
                    class_name="relative overflow-x-auto border rounded-lg",
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm",
            ),
        )
    )