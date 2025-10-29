import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.dashboard_state import DashboardState, Claim


def claim_row(claim: Claim) -> rx.Component:
    return rx.el.tr(
        rx.el.td(claim["id"], class_name="px-6 py-4"),
        rx.el.td(claim["type"], class_name="px-6 py-4"),
        rx.el.td(f"${claim['amount']:.2f}", class_name="px-6 py-4"),
        rx.el.td(claim["date_submitted"], class_name="px-6 py-4"),
        rx.el.td(
            rx.el.span(
                claim["status"],
                class_name=rx.match(
                    claim["status"],
                    (
                        "Approved",
                        "bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    ),
                    (
                        "Pending",
                        "bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    ),
                    (
                        "Rejected",
                        "bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    ),
                    "bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                ),
            ),
            class_name="px-6 py-4",
        ),
    )


def claims() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Claims Management", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Submit new claims and track their status.",
                class_name="text-gray-500 mb-8",
            ),
            rx.el.div(
                rx.el.h2("Submit a New Claim", class_name="text-xl font-semibold mb-4"),
                rx.el.form(
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Claim Type",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.input(
                                placeholder="e.g., Emergency Visit",
                                class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                            ),
                            class_name="flex-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Amount",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.input(
                                type="number",
                                placeholder="$0.00",
                                class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex gap-4 mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Description",
                            class_name="block text-sm font-medium text-gray-700",
                        ),
                        rx.el.textarea(
                            placeholder="Briefly describe the claim...",
                            class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.button(
                        "Submit Claim",
                        type="submit",
                        class_name="bg-violet-500 text-white px-6 py-2 rounded-md font-semibold hover:bg-violet-600",
                    ),
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm mb-8",
            ),
            rx.el.div(
                rx.el.h2("Your Claims", class_name="text-xl font-semibold mb-4"),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th("Claim ID", class_name="px-6 py-3 text-left"),
                                rx.el.th("Type", class_name="px-6 py-3 text-left"),
                                rx.el.th("Amount", class_name="px-6 py-3 text-left"),
                                rx.el.th(
                                    "Date Submitted", class_name="px-6 py-3 text-left"
                                ),
                                rx.el.th("Status", class_name="px-6 py-3 text-left"),
                            ),
                            class_name="bg-gray-50",
                        ),
                        rx.el.tbody(rx.foreach(DashboardState.claims, claim_row)),
                        class_name="w-full text-sm text-left rtl:text-right text-gray-500",
                    ),
                    class_name="relative overflow-x-auto border rounded-lg",
                ),
                class_name="bg-white p-6 rounded-lg border shadow-sm",
            ),
        )
    )