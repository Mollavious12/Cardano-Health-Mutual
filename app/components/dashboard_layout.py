import reflex as rx
from app.components.sidebar import sidebar


def dashboard_layout(main_content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            main_content,
            class_name="flex-1 flex flex-col p-6 bg-gray-50 font-['Inter']",
        ),
        class_name="flex min-h-screen w-full",
    )