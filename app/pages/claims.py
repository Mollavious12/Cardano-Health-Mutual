import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.claims_state import ClaimsState, Claim


def claim_row(claim: Claim) -> rx.Component:
    return rx.el.tr(
        rx.el.td(claim["id"].to_string()[:8], class_name="px-6 py-4 font-mono text-sm"),
        rx.el.td(claim["type"], class_name="px-6 py-4"),
        rx.el.td(f"${claim['amount']:.2f}", class_name="px-6 py-4"),
        rx.el.td(claim["date_submitted"].to_string()[:10], class_name="px-6 py-4"),
        rx.el.td(
            rx.el.span(
                claim["status"],
                class_name=rx.match(
                    claim["status"],
                    (
                        "Approved",
                        "bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    ),
                    (
                        "Pending",
                        "bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    ),
                    (
                        "Rejected",
                        "bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                    ),
                    "bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                ),
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.foreach(
                    claim["documents"],
                    lambda doc: rx.el.a(
                        rx.icon("file-text", class_name="h-4 w-4"),
                        href=rx.get_upload_url(doc),
                        target="_blank",
                    ),
                ),
                class_name="flex gap-2",
            ),
            class_name="px-6 py-4",
        ),
    )


def claims_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Submit a New Claim", class_name="text-xl font-semibold mb-4"),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Claim Type",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        name="claim_type",
                        placeholder="e.g., Emergency Visit",
                        class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                        required=True,
                    ),
                    class_name="flex-1",
                ),
                rx.el.div(
                    rx.el.label(
                        "Amount", class_name="block text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        name="claim_amount",
                        type="number",
                        placeholder="$0.00",
                        class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                        required=True,
                    ),
                    class_name="flex-1",
                ),
                class_name="flex flex-col md:flex-row gap-4 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Description", class_name="block text-sm font-medium text-gray-700"
                ),
                rx.el.textarea(
                    name="claim_description",
                    placeholder="Briefly describe the claim...",
                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                    required=True,
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Supporting Documents",
                    class_name="block text-sm font-medium text-gray-700 mb-2",
                ),
                rx.upload.root(
                    rx.el.div(
                        rx.icon(tag="cloud_upload", class_name="w-8 h-8 text-gray-500"),
                        rx.el.p("Drag & drop files here, or click to select files"),
                        class_name="text-center p-6 border-2 border-dashed rounded-lg cursor-pointer",
                    ),
                    id="upload_claim_docs",
                    multiple=True,
                    accept={
                        "application/pdf": [".pdf"],
                        "image/jpeg": [".jpg", ".jpeg"],
                        "image/png": [".png"],
                    },
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.foreach(
                        rx.selected_files("upload_claim_docs"),
                        lambda file: rx.el.div(
                            rx.el.p(file, class_name="text-sm"),
                            class_name="flex items-center justify-between p-2 bg-gray-50 border rounded",
                        ),
                    ),
                    class_name="space-y-2 mb-4",
                ),
                rx.el.button(
                    "Upload Documents",
                    on_click=ClaimsState.handle_upload(
                        rx.upload_files(upload_id="upload_claim_docs")
                    ),
                    type="button",
                    class_name="mb-4 text-sm font-medium text-violet-600 hover:text-violet-800",
                ),
            ),
            rx.el.button(
                rx.cond(
                    ClaimsState.is_loading,
                    rx.el.p("Submitting..."),
                    rx.el.p("Submit Claim"),
                ),
                type="submit",
                class_name="bg-violet-500 text-white px-6 py-2 rounded-md font-semibold hover:bg-violet-600 disabled:bg-gray-400",
                disabled=ClaimsState.is_loading,
            ),
            on_submit=ClaimsState.submit_claim,
            reset_on_submit=True,
        ),
        class_name="bg-white p-6 rounded-lg border shadow-sm mb-8",
    )


def claims_table() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Your Claims", class_name="text-xl font-semibold mb-4"),
        rx.el.div(
            rx.cond(
                ClaimsState.is_loading,
                rx.el.div(
                    rx.spinner(size="3"), class_name="w-full flex justify-center p-8"
                ),
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th("Claim ID", class_name="px-6 py-3 text-left"),
                            rx.el.th("Type", class_name="px-6 py-3 text-left"),
                            rx.el.th("Amount", class_name="px-6 py-3 text-left"),
                            rx.el.th(
                                "Date Submitted", class_name="px-6 py-3 text-left"
                            ),
                            rx.el.th("Status", class_name="px-6 py-3 text-left"),
                            rx.el.th("Documents", class_name="px-6 py-3 text-left"),
                        ),
                        class_name="bg-gray-50",
                    ),
                    rx.el.tbody(rx.foreach(ClaimsState.claims, claim_row)),
                    class_name="w-full text-sm text-left rtl:text-right text-gray-500",
                ),
            ),
            class_name="relative overflow-x-auto border rounded-lg",
        ),
        class_name="bg-white p-6 rounded-lg border shadow-sm",
    )


def claims() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h1("Claims Management", class_name="text-3xl font-bold mb-2"),
            rx.el.p(
                "Submit new claims and track their status.",
                class_name="text-gray-500 mb-8",
            ),
            claims_form(),
            claims_table(),
            on_mount=ClaimsState.get_claims,
        )
    )