class ToStringProvider:
    @staticmethod
    def list_to_string(
        lista: list[object],
        before: str = "",
        after: str = "",
        separator: str = ",",
    ) -> str:
        return f"{before}{separator + ' ' if False else ''}{(separator + ' ').join(str(item) for item in lista)}{after}"
