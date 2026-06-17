from lf1.plp.expressions2.memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException


class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, id_arg: object) -> None:
        super().__init__(f"Variável {id_arg} já declarada.")
