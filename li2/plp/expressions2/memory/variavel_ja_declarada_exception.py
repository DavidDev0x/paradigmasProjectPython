from li2.plp.expressions2.memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException


class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, identificador) -> None:
        super().__init__(f"Variável {identificador} já declarada.")
