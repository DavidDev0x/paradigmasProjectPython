from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression._runtime_checks import exigir
from le2.plp.expressions2.expression.exp_binaria import ExpBinaria
from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.valor import Valor
from le2.plp.expressions2.expression.valor_string import ValorString
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class ExpConcat(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "++")

    def avaliar(self, amb: AmbienteExecucao) -> Valor:
        esq = exigir(self.get_esq().avaliar(amb), ValorString, "string", self.get_operador())
        dir = exigir(self.get_dir().avaliar(amb), ValorString, "string", self.get_operador())
        return ValorString(esq.valor() + dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente: AmbienteCompilacao) -> bool:
        return self.get_esq().get_tipo(ambiente).e_string() and self.get_dir().get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente: AmbienteCompilacao) -> Tipo:
        return Tipo.TIPO_STRING
