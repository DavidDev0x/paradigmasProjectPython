from __future__ import annotations

from typing import Any

from lf1.plp.expressions2.memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException
from lf1.plp.expressions2.memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException


class StackHandler:
    def __init__(self) -> None:
        raise TypeError("StackHandler é uma classe utilitária e não deve ser instanciada.")

    @staticmethod
    def get_from_id(stack: list[dict[Any, Any]], id_arg: Any) -> Any:
        for escopo in reversed(stack):
            if id_arg in escopo:
                return escopo[id_arg]
        raise IdentificadorNaoDeclaradoException()

    @staticmethod
    def map_id_object(stack: list[dict[Any, Any]], id_arg: Any, obj: Any) -> None:
        if not stack:
            raise RuntimeError("Pilha vazia.")
        topo = stack[-1]
        if id_arg in topo:
            raise IdentificadorJaDeclaradoException()
        topo[id_arg] = obj
