from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.exp_binaria import ExpBinaria
from li2.plp.expressions2.expression.valor_string import ValorString


class ExpConcat(ExpBinaria):
    def __init__(self, esq, dir) -> None:
        super().__init__(esq, dir, "++")

    def avaliar(self, ambiente):
        esq = exigir_tipo(self.get_esq().avaliar(ambiente), ValorString, "++")
        dir = exigir_tipo(self.get_dir().avaliar(ambiente), ValorString, "++")
        return ValorString(esq.valor() + dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_string() and self.get_dir().get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.STRING

    def clone(self):
        return ExpConcat(self.get_esq().clone(), self.get_dir().clone())
