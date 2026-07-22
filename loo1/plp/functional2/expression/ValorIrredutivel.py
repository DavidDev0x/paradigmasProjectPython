from loo1.plp.expressions2.expression.Valor import Valor


class ValorIrredutivel(Valor):
    def avaliar(self, ambiente):
        return None

    def checa_tipo(self, ambiente) -> bool:
        return True

    def get_tipo(self, ambiente):
        return None

    def reduzir(self, ambiente):
        return self

    def clone(self):
        return self
