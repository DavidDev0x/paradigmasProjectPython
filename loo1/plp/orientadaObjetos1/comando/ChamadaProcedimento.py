from .Comando import Comando
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class ChamadaProcedimento(Comando):
    def __init__(self, procedimento, parametros_reais, valores_parametros=None):
        self._procedimento = procedimento
        self._parametros_reais = parametros_reais
        self._valores_parametros = valores_parametros

    def _bind_parameters(self, ambiente, parametros_formais):
        valores = self._valores_parametros
        if valores is None:
            valores = self._parametros_reais.avaliar(ambiente)
        while valores.length() > 0:
            if parametros_formais is None or parametros_formais.get_head() is None:
                raise ProcedimentoNaoDeclaradoException("<parâmetros incompatíveis>")
            ambiente.map(parametros_formais.get_head().get_id(), valores.get_head())
            parametros_formais = parametros_formais.get_tail()
            valores = valores.get_tail()
        return ambiente

    def executar(self, ambiente):
        ambiente.incrementa()
        try:
            self._bind_parameters(ambiente, self._procedimento.get_parametros_formais())
            return self._procedimento.get_comando().executar(ambiente)
        finally:
            ambiente.restaura()

    def checa_tipo(self, ambiente) -> bool:
        ambiente.incrementa()
        try:
            formais = self._procedimento.get_parametros_formais()
            tipos = self._parametros_reais.get_tipos(ambiente)
            if tipos.length() != formais.length():
                return False
            while tipos is not None and tipos.head() is not None:
                if formais is None or formais.get_head() is None:
                    return False
                if tipos.head() != formais.get_head().get_tipo():
                    return False
                tipos = tipos.tail()
                formais = formais.get_tail()
            return True
        finally:
            ambiente.restaura()
