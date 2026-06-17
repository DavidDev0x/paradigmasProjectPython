from __future__ import annotations

from typing import TYPE_CHECKING

from le2.plp.expressions2.memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException

if TYPE_CHECKING:
    from le2.plp.expressions2.expression.id import Id


class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, id_arg: Id) -> None:
        super().__init__(f"Variável {id_arg} já declarada.")
