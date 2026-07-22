from .DecProcedimento import DecProcedimento
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class DecProcedimentoComposta(DecProcedimento):
    def __init__(self, declaracao1, declaracao2):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def get_procedimento(self, identificador):
        try:
            return self._declaracao1.get_procedimento(identificador)
        except ProcedimentoNaoDeclaradoException:
            return self._declaracao2.get_procedimento(identificador)

    def checa_tipo(self, ambiente) -> bool:
        return self._declaracao1.checa_tipo(ambiente) and self._declaracao2.checa_tipo(ambiente)
