import reflex as rx
from app.states.dashboard_state import DashboardState
import reflex_clerk_api as clerk

NAV_ITEMS = [
    {"label": "Dashboard", "icon": "layout-dashboard", "href": "/dashboard"},
    {"label": "My Wallet", "icon": "wallet", "href": "/wallet"},
    {"label": "Health Coverage", "icon": "shield-check", "href": "/coverage"},
    {"label": "Claims", "icon": "file-text", "href": "/claims"},
    {"label": "Learning Hub", "icon": "book-open", "href": "/learning-hub"},
    {"label": "Mutual Engine", "icon": "coins", "href": "/mutual-engine"},
    {"label": "Community Chat", "icon": "message-circle", "href": "/community-chat"},
]
ADMIN_NAV_ITEMS = [{"label": "Admin Panel", "icon": "shield", "href": "/admin-panel"}]


def nav_item(item: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(item["icon"], class_name="h-5 w-5"),
        rx.cond(DashboardState.sidebar_collapsed, None, rx.el.span(item["label"])),
        href=item.get("href", "#"),
        class_name=rx.cond(
            DashboardState.sidebar_collapsed,
            "flex h-9 w-9 items-center justify-center rounded-lg text-gray-500 transition-colors hover:text-gray-900 md:h-8 md:w-8",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("heart-pulse", class_name="h-6 w-6 text-violet-500"),
                    rx.cond(
                        DashboardState.sidebar_collapsed,
                        None,
                        rx.el.span("CareChain", class_name="font-semibold"),
                    ),
                    href="/",
                    class_name="flex items-center gap-2 font-semibold",
                ),
                rx.el.button(
                    rx.icon("panel-left-close", class_name="h-5 w-5"),
                    on_click=DashboardState.toggle_sidebar,
                    class_name="rounded-full p-2 hover:bg-gray-100",
                    variant="ghost",
                ),
                class_name="flex h-16 items-center justify-between border-b px-4 shrink-0",
            ),
            rx.el.nav(
                rx.foreach(NAV_ITEMS, nav_item),
                rx.foreach(ADMIN_NAV_ITEMS, nav_item),
                class_name="flex-1 overflow-auto p-4 flex flex-col items-start gap-1",
            ),
            rx.el.div(
                clerk.user_button(after_sign_out_url="/"),
                rx.cond(
                    DashboardState.sidebar_collapsed,
                    None,
                    rx.el.div(
                        rx.el.p(
                            clerk.ClerkUser.first_name,
                            class_name="font-semibold text-sm",
                        ),
                        rx.el.p(
                            clerk.ClerkUser.email_address,
                            class_name="text-xs text-gray-500",
                        ),
                        class_name="flex flex-col",
                    ),
                ),
                class_name="flex items-center gap-3 p-4 border-t mt-auto",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name=rx.cond(
            DashboardState.sidebar_collapsed,
            "hidden md:flex flex-col border-r bg-gray-50/50 w-16 transition-all",
            "hidden md:flex flex-col border-r bg-gray-50/50 w-64 transition-all",
        ),
    )