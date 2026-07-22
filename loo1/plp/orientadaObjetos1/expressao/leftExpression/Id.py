from loo1.plp.expressions2.expression.Id import Id as IdBase
from .LeftExpression import LeftExpression


class Id(IdBase, LeftExpression):
    def __init__(self, str_name: str):
        super().__init__(str_name)

    def avaliar(self, ambiente):
        return ambiente.get(self)

    def checa_tipo(self, ambiente) -> bool:
        ambiente.get(self)
        return True

    def get_tipo(self, ambiente):
        return ambiente.get(self)

    def get_id(self) -> "Id":
        return self
