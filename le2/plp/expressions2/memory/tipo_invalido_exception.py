class TipoInvalidoException(TypeError):
    """Erro usado para impedir coerções dinâmicas do Python durante a execução."""

    def __init__(self, esperado: str, recebido: object, operador: str | None = None) -> None:
        op = f" no operador '{operador}'" if operador is not None else ""
        super().__init__(f"Tipo inválido{op}: esperado {esperado}, recebido {type(recebido).__name__}.")
