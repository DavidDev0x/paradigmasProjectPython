from __future__ import annotations

from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.id import Id
from le2.plp.expressions2.expression.valor import Valor
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao
from le2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException


class ExpDeclaracao(Expressao):
    def __init__(self, declarations: list[DecVariavel], expressao_arg: Expressao) -> None:
        if not isinstance(declarations, list):
            raise TypeError("declarations deve ser list[DecVariavel].")
        if not all(isinstance(dec, DecVariavel) for dec in declarations):
            raise TypeError("todos os itens de declarations devem ser DecVariavel.")
        if not isinstance(expressao_arg, Expressao):
            raise TypeError("expressao_arg deve implementar Expressao.")
        self._seq_dec_variavel = declarations
        self._expressao = expressao_arg

    def avaliar(self, ambiente: AmbienteExecucao) -> Valor:
        ambiente.incrementa()
        try:
            resolved_values = self._resolve_value_bindings(ambiente)
            self._include_value_bindings(ambiente, resolved_values)
            return self._expressao.avaliar(ambiente)
        finally:
            ambiente.restaura()

    def _include_value_bindings(self, ambiente: AmbienteExecucao, resolved_values: dict[Id, Valor]) -> None:
        for id_arg, valor in resolved_values.items():
            ambiente.map(id_arg, valor)

    def _resolve_value_bindings(self, ambiente: AmbienteExecucao) -> dict[Id, Valor]:
        resolved_values: dict[Id, Valor] = {}
        for declaration in self._seq_dec_variavel:
            id_arg = declaration.get_id()
            if id_arg in resolved_values:
                raise VariavelJaDeclaradaException(id_arg)
            resolved_values[id_arg] = declaration.get_expressao().avaliar(ambiente)
        return resolved_values

    def checa_tipo(self, ambiente: AmbienteCompilacao) -> bool:
        ambiente.incrementa()
        try:
            if not self._check_type_bindings(ambiente):
                return False
            resolved_types = self._resolve_type_bindings(ambiente)
            self._include_type_bindings(ambiente, resolved_types)
            return self._expressao.checa_tipo(ambiente)
        finally:
            ambiente.restaura()

    def _include_type_bindings(self, ambiente: AmbienteCompilacao, resolved_types: dict[Id, Tipo]) -> None:
        for id_arg, tipo in resolved_types.items():
            ambiente.map(id_arg, tipo)

    def _resolve_type_bindings(self, ambiente: AmbienteCompilacao) -> dict[Id, Tipo]:
        resolved_types: dict[Id, Tipo] = {}
        for declaration in self._seq_dec_variavel:
            id_arg = declaration.get_id()
            if id_arg in resolved_types:
                raise VariavelJaDeclaradaException(id_arg)
            resolved_types[id_arg] = declaration.get_expressao().get_tipo(ambiente)
        return resolved_types

    def _check_type_bindings(self, ambiente: AmbienteCompilacao) -> bool:
        for declaration in self._seq_dec_variavel:
            if not declaration.get_expressao().checa_tipo(ambiente):
                return False
        return True

    def get_tipo(self, ambiente: AmbienteCompilacao) -> Tipo:
        ambiente.incrementa()
        try:
            resolved_types = self._resolve_type_bindings(ambiente)
            self._include_type_bindings(ambiente, resolved_types)
            return self._expressao.get_tipo(ambiente)
        finally:
            ambiente.restaura()
