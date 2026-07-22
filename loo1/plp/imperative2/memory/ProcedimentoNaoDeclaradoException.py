from loo1.plp.expressions2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class ProcedimentoNaoDeclaradoException(IdentificadorNaoDeclaradoException):
    def __init__(self, identificador):
        super().__init__(f"Procedimento {identificador} não declarado.")
