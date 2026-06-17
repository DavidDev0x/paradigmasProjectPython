from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.declaration.dec_variavel import DecVariavel
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.expressions2.expression.valor import Valor
from lf1.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException


class ExpDeclaracao(Expressao):
    def __init__(self, declarations: list[DecVariavel], expressao_arg: Expressao) -> None:
        self._seqdec_variavel = list(declarations)
        self._expressao = expressao_arg

    def avaliar(self, ambiente: Any) -> Valor:
        ambiente.incrementa()
        try:
            resolved_values = self.resolve_value_bindings(ambiente)
            self.include_value_bindings(ambiente, resolved_values)
            return self._expressao.avaliar(ambiente)
        finally:
            ambiente.restaura()

    def include_value_bindings(self, ambiente: Any, resolved_values: dict[Id, Valor]) -> None:
        for id_arg, valor in resolved_values.items():
            ambiente.map(id_arg, valor)

    def resolve_value_bindings(self, ambiente: Any) -> dict[Id, Valor]:
        resolved_values: dict[Id, Valor] = {}
        for declaration in self._seqdec_variavel:
            if declaration.get_id() in resolved_values:
                raise VariavelJaDeclaradaException(declaration.get_id())
            resolved_values[declaration.get_id()] = declaration.get_expressao().avaliar(ambiente)
        return resolved_values

    def checa_tipo(self, ambiente: Any) -> bool:
        ambiente.incrementa()
        try:
            if not self.check_type_bindings(ambiente):
                return False
            resolved_types = self.resolve_type_bindings(ambiente)
            self.include_type_bindings(ambiente, resolved_types)
            return self._expressao.checa_tipo(ambiente)
        finally:
            ambiente.restaura()

    def include_type_bindings(self, ambiente: Any, resolved_types: dict[Id, Tipo]) -> None:
        for id_arg, tipo in resolved_types.items():
            ambiente.map(id_arg, tipo)

    def resolve_type_bindings(self, ambiente: Any) -> dict[Id, Tipo]:
        resolved_types: dict[Id, Tipo] = {}
        for declaration in self._seqdec_variavel:
            if declaration.get_id() in resolved_types:
                raise VariavelJaDeclaradaException(declaration.get_id())
            resolved_types[declaration.get_id()] = declaration.get_expressao().get_tipo(ambiente)
        return resolved_types

    def check_type_bindings(self, ambiente: Any) -> bool:
        return all(declaration.get_expressao().checa_tipo(ambiente) for declaration in self._seqdec_variavel)

    def get_tipo(self, ambiente: Any) -> Tipo:
        ambiente.incrementa()
        try:
            resolved_types = self.resolve_type_bindings(ambiente)
            self.include_type_bindings(ambiente, resolved_types)
            return self._expressao.get_tipo(ambiente)
        finally:
            ambiente.restaura()

    def get_seqdec_variavel(self) -> list[DecVariavel]:
        return self._seqdec_variavel

    def get_expressao(self) -> Expressao:
        return self._expressao
