from __future__ import annotations
from li1.plp.expressions2.memory.contexto_execucao import ContextoExecucao
from li1.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from .ambiente_execucao_imperativa import AmbienteExecucaoImperativa
from .entrada_vazia_exception import EntradaVaziaException
from .lista_valor import ListaValor

class ContextoExecucaoImperativa(ContextoExecucao, AmbienteExecucaoImperativa):
    def __init__(self, entrada: ListaValor | None) -> None:
        super().__init__()
        self._entrada = entrada
        self._saida = ListaValor()

    def read(self):
        if self._entrada is None or self._entrada.get_head() is None:
            raise EntradaVaziaException()
        aux = self._entrada.get_head()
        tail = self._entrada.get_tail()
        self._entrada = tail if isinstance(tail, ListaValor) else None
        return aux

    def get_saida(self) -> ListaValor:
        return self._saida

    def write(self, v) -> None:
        self._saida.write(v)

    def change_valor(self, id_arg, valor_id) -> None:
        for bloco in reversed(self.get_pilha()):
            if id_arg in bloco:
                bloco[id_arg] = valor_id
                return
        raise VariavelNaoDeclaradaException(id_arg)
