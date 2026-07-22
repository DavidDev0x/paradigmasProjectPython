from .IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, identificador: object):
        super().__init__(f"Variável {identificador} não declarada.")
