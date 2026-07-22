from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.exp_binaria import ExpBinaria
from li2.plp.expressions2.expression.valor_inteiro import ValorInteiro


class ExpSub(ExpBinaria):
    def __init__(self, esq, dir) -> None:
        super().__init__(esq, dir, "-")

    def avaliar(self, ambiente):
        esq = exigir_tipo(self.get_esq().avaliar(ambiente), ValorInteiro, "-")
        dir = exigir_tipo(self.get_dir().avaliar(ambiente), ValorInteiro, "-")
        return ValorInteiro(esq.valor() - dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_inteiro() and self.get_dir().get_tipo(ambiente).e_inteiro()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self):
        return ExpSub(self.get_esq().clone(), self.get_dir().clone())
