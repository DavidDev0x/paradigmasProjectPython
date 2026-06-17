from __future__ import annotations
from li1.plp.expressions2.memory.contexto_compilacao import ContextoCompilacao
from .ambiente_compilacao_imperativa import AmbienteCompilacaoImperativa
from .entrada_vazia_exception import EntradaVaziaException
from .lista_valor import ListaValor

class ContextoCompilacaoImperativa(ContextoCompilacao, AmbienteCompilacaoImperativa):
    def __init__(self, entrada: ListaValor | None) -> None:
        super().__init__()
        self._entrada = entrada

    def get_tipo_entrada(self):
        if self._entrada is None or self._entrada.get_head() is None:
            raise EntradaVaziaException()
        aux = self._entrada.get_head().get_tipo(self)
        tail = self._entrada.get_tail()
        self._entrada = tail if isinstance(tail, ListaValor) else None
        return aux
