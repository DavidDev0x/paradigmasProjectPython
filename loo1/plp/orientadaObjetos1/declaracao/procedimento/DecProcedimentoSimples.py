from .DecProcedimento import DecProcedimento
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class DecProcedimentoSimples(DecProcedimento):
    def __init__(self, nome, parametros_formais, comando):
        self._nome = nome
        self._parametros_formais = parametros_formais
        self._comando = comando

    def get_procedimento(self, nome):
        if self._nome == nome:
            from loo1.plp.orientadaObjetos1.comando.Procedimento import Procedimento
            return Procedimento(self._parametros_formais, self._comando)
        raise ProcedimentoNaoDeclaradoException(nome)

    def checa_tipo(self, ambiente) -> bool:
        if not self._parametros_formais.checa_tipo(ambiente):
            return False
        ambiente.map_parametros_procedimento(self._nome, self._parametros_formais)
        ambiente.incrementa()
        try:
            self._parametros_formais.declara_parametro(ambiente)
            return self._comando.checa_tipo(ambiente)
        finally:
            ambiente.restaura()
