import reflex as rx
import reflex_clerk_api as clerk


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("heart-pulse", class_name="h-6 w-6 text-violet-500"),
                    rx.el.span("CareChain", class_name="font-semibold text-lg"),
                    class_name="flex items-center gap-2",
                ),
                href="/",
            ),
            rx.el.nav(
                rx.el.a(
                    "Dashboard",
                    href="/dashboard",
                    class_name="text-sm font-medium text-gray-600 hover:text-gray-900",
                ),
                rx.el.a(
                    "Learning Hub",
                    href="#",
                    class_name="text-sm font-medium text-gray-600 hover:text-gray-900",
                ),
                rx.el.a(
                    "About",
                    href="#",
                    class_name="text-sm font-medium text-gray-600 hover:text-gray-900",
                ),
                rx.el.a(
                    "Contact",
                    href="#",
                    class_name="text-sm font-medium text-gray-600 hover:text-gray-900",
                ),
                class_name="hidden md:flex gap-6",
            ),
            rx.el.div(
                clerk.signed_out(
                    rx.el.div(
                        clerk.sign_in_button(
                            rx.el.button(
                                "Login",
                                class_name="bg-transparent border border-gray-300 text-gray-700 px-4 py-2 rounded-md text-sm font-medium hover:bg-gray-50 transition-colors",
                            )
                        ),
                        clerk.sign_up_button(
                            rx.el.button(
                                "Join a Mutual",
                                class_name="bg-violet-500 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-violet-600 transition-colors",
                            )
                        ),
                        class_name="flex items-center gap-4",
                    )
                ),
                clerk.signed_in(clerk.user_button(after_sign_out_url="/")),
                class_name="flex items-center gap-4",
            ),
            class_name="container mx-auto flex h-16 items-center justify-between px-4 md:px-6",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-sm border-b border-gray-200",
    )