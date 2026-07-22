class ProcedimentoNaoDeclaradoException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Procedimento não declarado." if identificador is None else f"Procedimento {identificador} não declarado."
        super().__init__(mensagem)
