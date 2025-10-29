import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("heart-pulse", class_name="h-6 w-6 text-violet-500"),
                        rx.el.span(
                            "CareChain",
                            class_name="font-semibold text-lg text-gray-800",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    href="/",
                ),
                rx.el.p(
                    "Mutual Access to Healthcare for All.",
                    class_name="text-sm text-gray-500 mt-2",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Navigate", class_name="text-sm font-semibold text-gray-900"
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Dashboard",
                            href="#",
                            class_name="text-sm text-gray-600 hover:text-gray-900",
                        ),
                        rx.el.a(
                            "Learning Hub",
                            href="#",
                            class_name="text-sm text-gray-600 hover:text-gray-900",
                        ),
                        rx.el.a(
                            "About Us",
                            href="#",
                            class_name="text-sm text-gray-600 hover:text-gray-900",
                        ),
                        rx.el.a(
                            "Contact",
                            href="#",
                            class_name="text-sm text-gray-600 hover:text-gray-900",
                        ),
                        class_name="flex flex-col gap-2 mt-4",
                    ),
                ),
                rx.el.div(
                    rx.el.h3("Legal", class_name="text-sm font-semibold text-gray-900"),
                    rx.el.div(
                        rx.el.a(
                            "Privacy Policy",
                            href="#",
                            class_name="text-sm text-gray-600 hover:text-gray-900",
                        ),
                        rx.el.a(
                            "Terms of Service",
                            href="#",
                            class_name="text-sm text-gray-600 hover:text-gray-900",
                        ),
                        class_name="flex flex-col gap-2 mt-4",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Follow Us", class_name="text-sm font-semibold text-gray-900"
                    ),
                    rx.el.div(
                        rx.el.a(rx.icon("twitter", class_name="h-5 w-5"), href="#"),
                        rx.el.a(rx.icon("facebook", class_name="h-5 w-5"), href="#"),
                        rx.el.a(rx.icon("linkedin", class_name="h-5 w-5"), href="#"),
                        class_name="flex gap-4 mt-4 text-gray-600",
                    ),
                ),
                class_name="grid grid-cols-2 md:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 px-4 md:px-6 py-12",
        ),
        rx.el.div(
            rx.el.p(
                f"© {2024} CareChain. All rights reserved.",
                class_name="text-sm text-gray-500",
            ),
            class_name="bg-gray-50 py-6 text-center",
        ),
        class_name="bg-white border-t",
    )