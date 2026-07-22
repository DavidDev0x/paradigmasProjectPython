from li2.plp.expressions2.memory.contexto_execucao import ContextoExecucao
from li2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from li2.plp.imperative1.memory.ambiente_execucao_imperativa import AmbienteExecucaoImperativa
from li2.plp.imperative1.memory.entrada_vazia_exception import EntradaVaziaException
from li2.plp.imperative1.memory.lista_valor import ListaValor


class ContextoExecucaoImperativa(ContextoExecucao, AmbienteExecucaoImperativa):
    def __init__(self, entrada) -> None:
        super().__init__()
        self._entrada = entrada
        self._saida = ListaValor()

    def read(self):
        if self._entrada is None or self._entrada.get_head() is None:
            raise EntradaVaziaException()
        valor = self._entrada.get_head()
        self._entrada = self._entrada.get_tail()
        return valor

    def get_saida(self) -> ListaValor:
        return self._saida

    def write(self, valor) -> None:
        self._saida.write(valor)

    def change_valor(self, id_arg, valor_id) -> None:
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                bloco[id_arg] = valor_id
                return
        raise VariavelNaoDeclaradaException(id_arg)

    def clone(self) -> "ContextoExecucaoImperativa":
        retorno = ContextoExecucaoImperativa(self._entrada)
        consolidado = {}
        for bloco in self._pilha:
            consolidado.update(bloco)
        retorno.set_pilha([consolidado])
        retorno._saida = ListaValor.from_iterable(self._saida)
        return retorno
