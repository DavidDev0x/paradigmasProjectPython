from lf1.plp.expressions2.memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException


class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id_arg: object) -> None:
        super().__init__(f"Variável {id_arg} não declarada.")
