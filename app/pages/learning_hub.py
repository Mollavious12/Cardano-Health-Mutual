import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.learning_hub_state import LearningHubState
from app.components.course_card import course_card


def learning_hub() -> rx.Component:
    """The learning hub page, displaying all available courses."""
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Learning Hub", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Empower yourself with knowledge about health and finance.",
                class_name="text-gray-500 mb-8",
            ),
            rx.el.div(
                rx.foreach(LearningHubState.courses, course_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
        )
    )