from li2.plp.expressions2.memory.contexto import Contexto
from li2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from li2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from li2.plp.imperative1.memory.contexto_execucao_imperativa import ContextoExecucaoImperativa
from li2.plp.imperative2.memory.ambiente_execucao_imperativa2 import AmbienteExecucaoImperativa2
from li2.plp.imperative2.memory.procedimento_ja_declarado_exception import ProcedimentoJaDeclaradoException
from li2.plp.imperative2.memory.procedimento_nao_declarado_exception import ProcedimentoNaoDeclaradoException


class ContextoExecucaoImperativa2(ContextoExecucaoImperativa, AmbienteExecucaoImperativa2):
    def __init__(self, entrada) -> None:
        super().__init__(entrada)
        self._contexto_procedimentos = Contexto()

    def incrementa(self) -> None:
        super().incrementa()
        self._contexto_procedimentos.incrementa()

    def restaura(self) -> None:
        super().restaura()
        self._contexto_procedimentos.restaura()

    def map_procedimento(self, id_arg, procedimento_id) -> None:
        try:
            self._contexto_procedimentos.map(id_arg, procedimento_id)
        except VariavelJaDeclaradaException as exc:
            raise ProcedimentoJaDeclaradoException(id_arg) from exc

    def get_procedimento(self, id_arg):
        try:
            return self._contexto_procedimentos.get(id_arg)
        except VariavelNaoDeclaradaException as exc:
            raise ProcedimentoNaoDeclaradoException(id_arg) from exc
