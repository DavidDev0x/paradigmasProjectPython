class VariavelNaoDeclaradaException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Variável não declarada." if identificador is None else f"Variável {identificador} não declarada."
        super().__init__(mensagem)
