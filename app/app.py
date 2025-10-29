import reflex as rx
from app.states.state import State
from app.components.navbar import navbar
from app.components.footer import footer
import reflex_clerk_api as clerk
import os


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Affordable. Inclusive. Smart Healthcare Access.",
                    class_name="text-4xl md:text-6xl font-bold text-gray-900 tracking-tighter",
                ),
                rx.el.p(
                    "Join a community-driven ecosystem for mutual healthcare access. Your health, our mutual strength.",
                    class_name="max-w-xl mt-6 text-lg text-gray-600",
                ),
                rx.el.div(
                    clerk.sign_up_button(
                        rx.el.button(
                            "Join a Mutual",
                            class_name="bg-violet-500 text-white px-6 py-3 rounded-md font-semibold hover:bg-violet-600 transition-colors",
                        )
                    ),
                    rx.el.button(
                        "Learn Health Finance",
                        variant="outline",
                        class_name="bg-transparent border border-gray-300 text-gray-700 px-6 py-3 rounded-md font-semibold hover:bg-gray-50 transition-colors",
                    ),
                    class_name="flex flex-col sm:flex-row gap-4 mt-8",
                ),
                class_name="flex flex-col items-center text-center",
            ),
            class_name="container mx-auto px-4 md:px-6 py-24 lg:py-32",
        ),
        class_name="bg-gray-50",
    )


def how_it_works_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "How It Works",
                    class_name="text-3xl font-bold tracking-tighter sm:text-4xl",
                ),
                rx.el.p(
                    "A simple, transparent process to secure your health.",
                    class_name="mt-4 text-gray-500 md:text-xl",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("users", class_name="h-10 w-10 text-violet-500"),
                    rx.el.h3(
                        "Mutual Contributions", class_name="text-xl font-semibold mt-4"
                    ),
                    rx.el.p(
                        "Members contribute small, manageable amounts into a collective pool.",
                        class_name="mt-2 text-gray-500",
                    ),
                    class_name="p-6 rounded-lg bg-white border border-gray-200",
                ),
                rx.el.div(
                    rx.icon("shield-check", class_name="h-10 w-10 text-violet-500"),
                    rx.el.h3(
                        "Health Coverage", class_name="text-xl font-semibold mt-4"
                    ),
                    rx.el.p(
                        "The pooled funds are used to cover verified health claims from members.",
                        class_name="mt-2 text-gray-500",
                    ),
                    class_name="p-6 rounded-lg bg-white border border-gray-200",
                ),
                rx.el.div(
                    rx.icon("area-chart", class_name="h-10 w-10 text-violet-500"),
                    rx.el.h3(
                        "Real-Time Transparency",
                        class_name="text-xl font-semibold mt-4",
                    ),
                    rx.el.p(
                        "Track all contributions and claim payouts on a transparent dashboard.",
                        class_name="mt-2 text-gray-500",
                    ),
                    class_name="p-6 rounded-lg bg-white border border-gray-200",
                ),
                class_name="grid md:grid-cols-3 gap-8 mt-12",
            ),
            class_name="container mx-auto px-4 md:px-6 py-16 md:py-24",
        )
    )


def community_impact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(State.formatted_members, class_name="text-4xl font-bold"),
                    rx.el.p("Active Members", class_name="text-gray-500"),
                    class_name="text-center",
                ),
                rx.el.div(
                    rx.el.p(State.formatted_funds, class_name="text-4xl font-bold"),
                    rx.el.p("Funds Raised", class_name="text-gray-500"),
                    class_name="text-center",
                ),
                rx.el.div(
                    rx.el.p(State.formatted_lives, class_name="text-4xl font-bold"),
                    rx.el.p("Lives Supported", class_name="text-gray-500"),
                    class_name="text-center",
                ),
                class_name="grid grid-cols-1 sm:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 md:px-6 py-16 md:py-24",
        ),
        class_name="bg-gray-50",
    )


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero_section(),
        how_it_works_section(),
        community_impact_section(),
        footer(),
        class_name="font-['Inter'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
from app.pages.dashboard import dashboard
from app.pages.wallet import wallet
from app.pages.coverage import coverage
from app.pages.claims import claims
from app.pages.profile import profile

clerk.wrap_app(
    app,
    publishable_key=os.environ.get("CLERK_PUBLISHABLE_KEY"),
    secret_key=os.environ.get("CLERK_SECRET_KEY"),
    register_user_state=True,
)
app.add_page(index)
app.add_page(dashboard)
app.add_page(wallet)
app.add_page(coverage)
app.add_page(claims)
app.add_page(profile)
clerk.add_sign_in_page(app)
clerk.add_sign_up_page(app)