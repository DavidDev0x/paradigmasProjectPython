from __future__ import annotations

from typing import Any

from lf1.plp.expressions2.expression.expressao import Expressao


class Id(Expressao):
    def __init__(self, str_name: str) -> None:
        if type(str_name) is not str:
            raise TypeError("Id exige nome do identificador como str.")
        self._id_name = str_name

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, Id) and obj._id_name == self._id_name

    def __hash__(self) -> int:
        return hash(self._id_name)

    def __str__(self) -> str:
        return self._id_name

    def __repr__(self) -> str:
        return f"Id({self._id_name!r})"

    def avaliar(self, ambiente: Any) -> Any:
        return ambiente.get(self)

    def checa_tipo(self, amb: Any) -> bool:
        amb.get(self)
        return True

    def get_tipo(self, amb: Any) -> Any:
        return amb.get(self)

    def get_id_name(self) -> str:
        return self._id_name

    def set_id_name(self, id_name: str) -> None:
        if type(id_name) is not str:
            raise TypeError("id_name deve ser str.")
        self._id_name = id_name
