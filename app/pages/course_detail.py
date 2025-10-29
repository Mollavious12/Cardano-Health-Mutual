import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.learning_hub_state import LearningHubState, Course


def course_content_placeholder() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Course Content Coming Soon", class_name="text-2xl font-bold mb-4"),
        rx.el.p(
            "This section will feature video lessons, articles, and quizzes to help you learn.",
            class_name="text-gray-600 mb-6",
        ),
        rx.el.div(
            rx.el.div(class_name="bg-gray-200 h-8 w-3/4 rounded mb-4 animate-pulse"),
            rx.el.div(class_name="bg-gray-200 h-4 w-full rounded mb-2 animate-pulse"),
            rx.el.div(class_name="bg-gray-200 h-4 w-5/6 rounded animate-pulse"),
            class_name="mt-8",
        ),
        rx.el.div(
            rx.el.div(class_name="bg-gray-200 h-8 w-3/4 rounded mb-4 animate-pulse"),
            rx.el.div(class_name="bg-gray-200 h-4 w-full rounded mb-2 animate-pulse"),
            rx.el.div(class_name="bg-gray-200 h-4 w-5/6 rounded animate-pulse"),
            class_name="mt-8",
        ),
        class_name="bg-white p-8 rounded-lg border shadow-sm mt-8",
    )


def course_detail() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1(
                f"Course: {LearningHubState.router.page.params.get('course_id', 'Not Found')}",
                class_name="text-3xl font-bold mb-2",
            ),
            rx.el.p(
                "Dive deep into the course material.", class_name="text-gray-500 mb-8"
            ),
            course_content_placeholder(),
        )
    )