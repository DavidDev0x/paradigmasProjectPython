class ObjetoNaoDeclaradoException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Objeto não declarado." if identificador is None else f"Objeto {identificador} não declarado."
        super().__init__(mensagem)
