import reflex as rx


class State(rx.State):
    """The base state for the app."""

    members: int = 1250
    funds_raised: int = 50000
    lives_supported: int = 2500

    @rx.var
    def formatted_members(self) -> str:
        return f"{self.members:,}"

    @rx.var
    def formatted_funds(self) -> str:
        return f"${self.funds_raised:,}"

    @rx.var
    def formatted_lives(self) -> str:
        return f"{self.lives_supported:,}"