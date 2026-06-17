from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.functional1.util.restrict_types_visitor import RestrictTypesVisitor


class ValorFuncao:
    def __init__(self, args_id: list[Id], exp: Expressao) -> None:
        self._args_id = list(args_id)
        self._exp = exp

    def get_lista_id(self) -> list[Id]:
        return self._args_id

    def get_exp(self) -> Expressao:
        return self._exp

    def get_aridade(self) -> int:
        return len(self._args_id)

    def checa_tipo(self, ambiente: Any) -> bool:
        tipo_funcao = self.get_tipo(ambiente)
        ambiente.incrementa()
        try:
            tipo_atual = tipo_funcao
            for id_arg in self._args_id:
                ambiente.map(id_arg, Tipo(tipo_atual.get()))
                tipo_atual = tipo_atual.get_prox()
                if tipo_atual is None:
                    return False
            return self._exp.checa_tipo(ambiente)
        finally:
            ambiente.restaura()

    def get_tipo(self, ambiente: Any) -> Tipo:
        map_id_tipo: dict[Id, Tipo] = {id_arg: Tipo() for id_arg in self._args_id}
        ids_arg = list(self._args_id)

        RestrictTypesVisitor.visit(self._exp, ambiente, map_id_tipo, Tipo())

        ambiente.incrementa()
        try:
            for id_arg, tipo in map_id_tipo.items():
                ambiente.map(id_arg, tipo)
            result = self._exp.get_tipo(ambiente)
            for id_arg in reversed(ids_arg):
                result = Tipo(map_id_tipo[id_arg].get(), result)
            return result
        finally:
            ambiente.restaura()
