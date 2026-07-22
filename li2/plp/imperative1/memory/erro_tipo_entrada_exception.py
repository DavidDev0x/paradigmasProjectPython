class ErroTipoEntradaException(Exception):
    def __init__(self, mensagem: str = "Tipo do valor de entrada lido incompatível") -> None:
        super().__init__(mensagem)
