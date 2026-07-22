from .Comando import Comando
from .ChamadaProcedimento import ChamadaProcedimento
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ChamadaMetodo(Comando):
    def __init__(self, expressao, nome_metodo, parametros_reais):
        self._expressao = expressao
        self._nome_metodo = nome_metodo
        self._parametros_reais = parametros_reais

    def executar(self, ambiente):
        referencia = self._expressao.avaliar(ambiente)
        if not isinstance(referencia, ValorRef):
            raise ErroTipoException("Chamada de método exige uma referência de objeto.")
        objeto = ambiente.get_objeto(referencia)
        metodo = ambiente.get_def_classe(objeto.get_classe()).get_metodo(self._nome_metodo)
        auxiliar = ContextoExecucaoOO1(ambiente)
        auxiliar.change_valor(Id("this"), referencia)
        valores = self._parametros_reais.avaliar(ambiente)
        ChamadaProcedimento(metodo, self._parametros_reais, valores).executar(auxiliar)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        try:
            tipo_classe = self._expressao.get_tipo(ambiente)
            metodo = ambiente.get_def_classe(tipo_classe.get_tipo()).get_metodo(self._nome_metodo)
            ambiente.incrementa()
            try:
                ambiente.map(Id("this"), tipo_classe)
                return ChamadaProcedimento(metodo, self._parametros_reais).checa_tipo(ambiente)
            finally:
                ambiente.restaura()
        except Exception:
            return False
