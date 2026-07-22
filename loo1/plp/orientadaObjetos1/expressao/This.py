from .Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class This(Expressao):
    _ID_THIS = Id("this")

    def avaliar(self, ambiente):
        return ambiente.get(self._ID_THIS)

    def checa_tipo(self, ambiente) -> bool:
        ambiente.get(self._ID_THIS)
        return True

    def get_tipo(self, ambiente):
        return ambiente.get(self._ID_THIS)
