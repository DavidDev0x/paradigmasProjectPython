from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.exp_unaria import ExpUnaria
from li2.plp.expressions2.expression.valor_booleano import ValorBooleano


class ExpNot(ExpUnaria):
    def __init__(self, exp) -> None:
        super().__init__(exp, "not")

    def avaliar(self, ambiente):
        valor = exigir_tipo(self.get_exp().avaliar(ambiente), ValorBooleano, "not")
        return ValorBooleano(not valor.valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_exp().get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self):
        return ExpNot(self.get_exp().clone())
