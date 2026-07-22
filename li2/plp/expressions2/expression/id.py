from li2.plp.expressions2.expression.expressao import Expressao
from li2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException


class Id(Expressao):
    def __init__(self, id_name: str) -> None:
        if type(id_name) is not str or not id_name:
            raise ValueError("O identificador deve possuir um nome não vazio.")
        self._id_name = id_name

    def avaliar(self, ambiente):
        return ambiente.get(self)

    def checa_tipo(self, ambiente) -> bool:
        ambiente.get(self)
        return True

    def get_tipo(self, ambiente):
        return ambiente.get(self)

    def get_id_name(self) -> str:
        return self._id_name

    def set_id_name(self, id_name: str) -> None:
        if type(id_name) is not str or not id_name:
            raise ValueError("O identificador deve possuir um nome não vazio.")
        self._id_name = id_name

    def reduzir(self, ambiente):
        try:
            return ambiente.get(self).clone()
        except VariavelNaoDeclaradaException:
            return self

    def clone(self) -> "Id":
        return self

    def __str__(self) -> str:
        return self._id_name

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, Id) and self._id_name == outro._id_name

    def __hash__(self) -> int:
        return hash(self._id_name)
