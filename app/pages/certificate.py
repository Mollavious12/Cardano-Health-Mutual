import reflex as rx
from app.components.dashboard_layout import dashboard_layout
import reflex_clerk_api as clerk
from app.states.course_state import CourseState


def certificate() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Certificate of Completion",
                    class_name="text-4xl font-bold text-center text-gray-800",
                ),
                rx.el.p("This certifies that", class_name="text-center text-lg mt-8"),
                rx.el.p(
                    f"{clerk.ClerkUser.first_name} {clerk.ClerkUser.last_name}",
                    class_name="text-3xl font-semibold text-center text-violet-600 mt-2",
                ),
                rx.el.p(
                    "has successfully completed the course",
                    class_name="text-center text-lg mt-4",
                ),
                rx.el.p(
                    CourseState.course["title"],
                    class_name="text-2xl font-bold text-center mt-2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Date of Completion", class_name="text-sm text-gray-500"
                        ),
                        rx.el.p("2024-05-24", class_name="font-semibold"),
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Issuing Authority", class_name="text-sm text-gray-500"
                        ),
                        rx.el.p("CareChain", class_name="font-semibold"),
                    ),
                    class_name="flex justify-between mt-16 pt-4 border-t",
                ),
                class_name="bg-white p-12 rounded-lg border-2 border-dashed border-violet-300 relative shadow-lg",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("download", class_name="mr-2"),
                    "Download Certificate",
                    on_click=rx.download(
                        data=f"Certificate for {CourseState.course['title']}",
                        filename="certificate.txt",
                    ),
                    class_name="mt-8 bg-violet-500 text-white px-6 py-3 rounded-md font-semibold hover:bg-violet-600 transition-colors",
                ),
                class_name="flex justify-center",
            ),
            class_name="max-w-4xl mx-auto py-12",
        )
    )