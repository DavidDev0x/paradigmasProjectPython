class ToStringProvider:
    @staticmethod
    def list_to_string(
        lista: list,
        separador: str,
        antes: str = "",
        depois: str = "",
    ) -> str:
        return f"{antes}{(separador + ' ').join(str(item) for item in lista)}{depois}"
