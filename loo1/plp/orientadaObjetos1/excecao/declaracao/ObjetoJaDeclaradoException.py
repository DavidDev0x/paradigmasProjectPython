class ObjetoJaDeclaradoException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Objeto da classe já declarado." if identificador is None else f"Objeto da classe {identificador} já declarado."
        super().__init__(mensagem)
