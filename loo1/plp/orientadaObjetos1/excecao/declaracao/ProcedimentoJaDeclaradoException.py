class ProcedimentoJaDeclaradoException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Procedimento já declarado." if identificador is None else f"Procedimento {identificador} já declarado."
        super().__init__(mensagem)
