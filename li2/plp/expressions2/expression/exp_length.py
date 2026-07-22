from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.exp_unaria import ExpUnaria
from li2.plp.expressions2.expression.valor_inteiro import ValorInteiro
from li2.plp.expressions2.expression.valor_string import ValorString


class ExpLength(ExpUnaria):
    def __init__(self, exp) -> None:
        super().__init__(exp, "length")

    def avaliar(self, ambiente):
        valor = exigir_tipo(self.get_exp().avaliar(ambiente), ValorString, "length")
        return ValorInteiro(len(valor.valor()))

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_exp().get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self):
        return ExpLength(self.get_exp().clone())
