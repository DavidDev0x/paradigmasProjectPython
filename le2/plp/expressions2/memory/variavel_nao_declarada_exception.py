from __future__ import annotations

from typing import TYPE_CHECKING

from le2.plp.expressions2.memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException

if TYPE_CHECKING:
    from le2.plp.expressions2.expression.id import Id


class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id_arg: Id) -> None:
        super().__init__(f"Variável {id_arg} não declarada.")
