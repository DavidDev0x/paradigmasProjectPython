from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.exp_binaria import ExpBinaria
from li2.plp.expressions2.expression.valor_booleano import ValorBooleano


class ExpOr(ExpBinaria):
    def __init__(self, esq, dir) -> None:
        super().__init__(esq, dir, "or")

    def avaliar(self, ambiente):
        esq = exigir_tipo(self.get_esq().avaliar(ambiente), ValorBooleano, "or")
        if esq.valor():
            return ValorBooleano(True)
        dir = exigir_tipo(self.get_dir().avaliar(ambiente), ValorBooleano, "or")
        return ValorBooleano(dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_booleano() and self.get_dir().get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self):
        return ExpOr(self.get_esq().clone(), self.get_dir().clone())
