import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.dashboard_state import DashboardState, Transaction


def transaction_row(transaction: Transaction) -> rx.Component:
    return rx.el.tr(
        rx.el.td(transaction["date"], class_name="px-6 py-4"),
        rx.el.td(transaction["description"], class_name="px-6 py-4"),
        rx.el.td(f"${transaction['amount']:.2f}", class_name="px-6 py-4"),
        rx.el.td(
            rx.el.span(
                transaction["status"],
                class_name=rx.cond(
                    transaction["status"] == "Completed",
                    "bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    "bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                ),
            ),
            class_name="px-6 py-4",
        ),
    )


def wallet() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("My Wallet", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Track your contributions and balance.", class_name="text-gray-500 mb-8"
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p("Current Balance", class_name="text-gray-600"),
                    rx.el.p(
                        f"${DashboardState.balance.to_string()}",
                        class_name="text-4xl font-bold",
                    ),
                ),
                rx.el.button(
                    "Add Funds",
                    class_name="bg-violet-500 text-white px-6 py-3 rounded-md font-semibold hover:bg-violet-600",
                ),
                class_name="flex justify-between items-center bg-white p-6 rounded-lg border shadow-sm mb-8",
            ),
            rx.el.div(
                rx.el.h2(
                    "Transaction History", class_name="text-xl font-semibold mb-4"
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
                            rx.foreach(DashboardState.transactions, transaction_row)
                        ),
                        class_name="w-full text-sm text-left rtl:text-right text-gray-500",
                    ),
                    class_name="relative overflow-x-auto border rounded-lg",
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm",
            ),
        )
    )