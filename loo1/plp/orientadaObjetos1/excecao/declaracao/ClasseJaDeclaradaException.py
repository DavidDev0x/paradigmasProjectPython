class ClasseJaDeclaradaException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Classe já declarada." if identificador is None else f"Classe {identificador} já declarada."
        super().__init__(mensagem)
