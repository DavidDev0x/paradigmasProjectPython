from li2.plp.expressions2.memory.contexto_compilacao import ContextoCompilacao
from li2.plp.imperative1.memory.ambiente_compilacao_imperativa import AmbienteCompilacaoImperativa
from li2.plp.imperative1.memory.entrada_vazia_exception import EntradaVaziaException


class ContextoCompilacaoImperativa(ContextoCompilacao, AmbienteCompilacaoImperativa):
    def __init__(self, entrada) -> None:
        super().__init__()
        self._entrada = entrada

    def get_tipo_entrada(self):
        if self._entrada is None or self._entrada.get_head() is None:
            raise EntradaVaziaException()
        valor = self._entrada.get_head()
        self._entrada = self._entrada.get_tail()
        return valor.get_tipo(self)
