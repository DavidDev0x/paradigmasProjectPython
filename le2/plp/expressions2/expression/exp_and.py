from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression._runtime_checks import exigir
from le2.plp.expressions2.expression.exp_binaria import ExpBinaria
from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.valor import Valor
from le2.plp.expressions2.expression.valor_booleano import ValorBooleano
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class ExpAnd(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "and")

    def avaliar(self, amb: AmbienteExecucao) -> Valor:
        esq = exigir(self.get_esq().avaliar(amb), ValorBooleano, "booleano", self.get_operador())
        if not esq.valor():
            return ValorBooleano(False)
        dir = exigir(self.get_dir().avaliar(amb), ValorBooleano, "booleano", self.get_operador())
        return ValorBooleano(esq.valor() and dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente: AmbienteCompilacao) -> bool:
        return self.get_esq().get_tipo(ambiente).e_booleano() and self.get_dir().get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente: AmbienteCompilacao) -> Tipo:
        return Tipo.TIPO_BOOLEANO
