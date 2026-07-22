from .Expressao import Expressao
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class Id(Expressao):
    def __init__(self, id_name: str):
        if type(id_name) is not str or not id_name:
            raise ValueError("O nome do identificador deve ser uma string não vazia.")
        self._id_name = id_name

    def __str__(self) -> str:
        return self._id_name

    def __repr__(self) -> str:
        return f"Id({self._id_name!r})"

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
            raise ValueError("O nome do identificador deve ser uma string não vazia.")
        self._id_name = id_name

    def __hash__(self) -> int:
        return hash(self._id_name)

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, Id) and self._id_name == outro._id_name

    def reduzir(self, ambiente):
        try:
            valor = ambiente.get(self)
        except VariavelNaoDeclaradaException:
            return self
        from loo1.plp.functional2.expression.ValorIrredutivel import ValorIrredutivel
        return self if isinstance(valor, ValorIrredutivel) else valor.clone()

    def clone(self) -> "Id":
        return self
