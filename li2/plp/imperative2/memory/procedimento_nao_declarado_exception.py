from li2.plp.expressions2.memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException


class ProcedimentoNaoDeclaradoException(IdentificadorNaoDeclaradoException):
    def __init__(self, identificador) -> None:
        super().__init__(f"Procedimento {identificador} não declarado.")
