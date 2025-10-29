import reflex as rx
from app.states.learning_hub_state import Course


def course_card(course: Course) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.div(
                rx.image(
                    src=course["image_url"], class_name="object-cover w-full h-40"
                ),
                rx.el.div(
                    rx.el.h3(course["title"], class_name="text-lg font-semibold"),
                    rx.el.p(
                        course["description"], class_name="text-sm text-gray-500 mt-1"
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                class_name="bg-violet-500 h-2 rounded-full",
                                style={"width": f"{course['progress']}%"},
                            ),
                            class_name="w-full bg-gray-200 rounded-full h-2 mt-4",
                        ),
                        rx.el.p(
                            f"{course['progress']}% Complete",
                            class_name="text-xs text-gray-500 mt-1",
                        ),
                        class_name="mt-4",
                    ),
                    class_name="p-4",
                ),
                class_name="bg-white rounded-lg overflow-hidden border border-gray-200 hover:shadow-lg transition-shadow",
            ),
            href=f"/learning-hub/{course['id']}",
        )
    )