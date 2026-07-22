from li2.plp.expressions2.memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException


class ProcedimentoJaDeclaradoException(IdentificadorJaDeclaradoException):
    def __init__(self, identificador) -> None:
        super().__init__(f"Procedimento {identificador} já declarado.")
