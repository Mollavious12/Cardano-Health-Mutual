import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.dashboard_state import DashboardState, HealthPlan


def health_plan_card(plan: HealthPlan) -> rx.Component:
    return rx.el.div(
        rx.el.h3(plan["name"], class_name="text-xl font-bold"),
        rx.el.p(plan["coverage"], class_name="text-gray-600 my-2"),
        rx.el.div(
            rx.el.p(
                f"${plan['contribution']:.2f}/month", class_name="text-lg font-semibold"
            ),
            rx.el.button(
                "Join Plan",
                class_name="bg-green-500 text-white px-4 py-2 rounded-md font-semibold hover:bg-green-600",
            ),
            class_name="flex justify-between items-center mt-4",
        ),
        class_name="bg-white p-6 rounded-lg border shadow-sm",
    )


def coverage() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Health Coverage", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Explore and join available mutual health plans.",
                class_name="text-gray-500 mb-8",
            ),
            rx.el.div(
                rx.foreach(DashboardState.health_plans, health_plan_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
        )
    )