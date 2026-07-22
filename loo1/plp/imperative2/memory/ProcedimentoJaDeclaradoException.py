from loo1.plp.expressions2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class ProcedimentoJaDeclaradoException(IdentificadorJaDeclaradoException):
    def __init__(self, identificador):
        super().__init__(f"Procedimento {identificador} já declarado.")
