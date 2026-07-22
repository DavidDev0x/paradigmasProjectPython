from .IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, identificador: object):
        super().__init__(f"Variável {identificador} já declarada.")
