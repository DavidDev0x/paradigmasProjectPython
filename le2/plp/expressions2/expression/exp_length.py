from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression._runtime_checks import exigir
from le2.plp.expressions2.expression.exp_unaria import ExpUnaria
from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.valor import Valor
from le2.plp.expressions2.expression.valor_inteiro import ValorInteiro
from le2.plp.expressions2.expression.valor_string import ValorString
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class ExpLength(ExpUnaria):
    def __init__(self, exp: Expressao) -> None:
        super().__init__(exp, "length")

    def avaliar(self, amb: AmbienteExecucao) -> Valor:
        exp = exigir(self.get_exp().avaliar(amb), ValorString, "string", self.get_operador())
        return ValorInteiro(len(exp.valor()))

    def checa_tipo_elemento_terminal(self, amb: AmbienteCompilacao) -> bool:
        return self.get_exp().get_tipo(amb).e_string()

    def get_tipo(self, amb: AmbienteCompilacao) -> Tipo:
        return Tipo.TIPO_INTEIRO
