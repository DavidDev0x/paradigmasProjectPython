class VariavelJaDeclaradaException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Variável já declarada." if identificador is None else f"Variável {identificador} já declarada."
        super().__init__(mensagem)
