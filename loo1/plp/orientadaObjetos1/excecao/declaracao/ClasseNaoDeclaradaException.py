class ClasseNaoDeclaradaException(Exception):
    def __init__(self, identificador=None):
        mensagem = "Classe não declarada." if identificador is None else f"Classe {identificador} não declarada."
        super().__init__(mensagem)
