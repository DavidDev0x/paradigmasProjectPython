from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.expressions2.expression.valor import Valor
from lf1.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from lf1.plp.functional1.declaration.declaracao_funcional import DeclaracaoFuncional
from lf1.plp.functional1.memory.ambiente_execucao_funcional import AmbienteExecucaoFuncional
from lf1.plp.functional1.util.valor_funcao import ValorFuncao


class ExpDeclaracao(Expressao):
    def __init__(self, declaracoes_funcionais: list[DeclaracaoFuncional], expressao_arg: Expressao) -> None:
        self._seqdec_funcional = list(declaracoes_funcionais)
        self._expressao = expressao_arg

    def __str__(self) -> str:
        return f"let {self._seqdec_funcional}\nin\n{self._expressao}"

    def avaliar(self, ambiente_funcional: Any) -> Valor:
        if not isinstance(ambiente_funcional, AmbienteExecucaoFuncional):
            raise TypeError("ExpDeclaracao funcional exige AmbienteExecucaoFuncional.")
        ambiente = ambiente_funcional
        ambiente.incrementa()
        try:
            aux_id_valor: dict[Id, Valor] = {}
            aux_id_valor_funcao: dict[Id, ValorFuncao] = {}
            self.resolve_bindings(ambiente, aux_id_valor, aux_id_valor_funcao)
            self.include_bindings(ambiente, aux_id_valor, aux_id_valor_funcao)
            return self._expressao.avaliar(ambiente)
        finally:
            ambiente.restaura()

    def include_bindings(self, ambiente: Any, aux_id_valor: dict[Id, Valor], aux_id_valor_funcao: dict[Id, ValorFuncao]) -> None:
        for id_arg, valor in aux_id_valor.items():
            ambiente.map(id_arg, valor)
        for id_arg, valor_funcao in aux_id_valor_funcao.items():
            ambiente.map_funcao(id_arg, valor_funcao)

    def resolve_bindings(self, ambiente: Any, aux_id_valor: dict[Id, Valor], aux_id_valor_funcao: dict[Id, ValorFuncao]) -> None:
        vistos: set[Id] = set()
        for dec_funcional in self._seqdec_funcional:
            if dec_funcional.get_id() in vistos:
                raise VariavelJaDeclaradaException(dec_funcional.get_id())
            vistos.add(dec_funcional.get_id())
            if dec_funcional.get_aridade() == 0:
                aux_id_valor[dec_funcional.get_id()] = dec_funcional.get_expressao().avaliar(ambiente)
            else:
                aux_id_valor_funcao[dec_funcional.get_id()] = dec_funcional.get_funcao()

    def checa_tipo(self, ambiente: Any) -> bool:
        ambiente.incrementa()
        try:
            result = self.check_type_bindings(ambiente)
            if result:
                resolved_types = self.resolve_type_bindings(ambiente)
                self.include_type_bindings(ambiente, resolved_types)
                result = self._expressao.checa_tipo(ambiente)
            return result
        finally:
            ambiente.restaura()

    def resolve_type_bindings(self, ambiente: Any) -> dict[Id, Tipo]:
        resolved_types: dict[Id, Tipo] = {}
        for dec_funcional in self._seqdec_funcional:
            if dec_funcional.get_id() in resolved_types:
                raise VariavelJaDeclaradaException(dec_funcional.get_id())
            resolved_types[dec_funcional.get_id()] = dec_funcional.get_tipo(ambiente)
        return resolved_types

    def check_type_bindings(self, ambiente: Any) -> bool:
        return all(dec_funcional.checa_tipo(ambiente) for dec_funcional in self._seqdec_funcional)

    def include_type_bindings(self, ambiente: Any, resolved_types: dict[Id, Tipo]) -> None:
        for id_arg, tipo in resolved_types.items():
            ambiente.map(id_arg, tipo)

    def get_tipo(self, ambiente: Any) -> Tipo:
        ambiente.incrementa()
        try:
            for dec_funcional in self._seqdec_funcional:
                if dec_funcional.get_aridade() == 0:
                    ambiente.map(dec_funcional.get_id(), dec_funcional.get_expressao().get_tipo(ambiente))
                else:
                    tipo = dec_funcional.get_funcao().get_tipo(ambiente)
                    if tipo != Tipo.TIPO_INDEFINIDO:
                        ambiente.map(dec_funcional.get_id(), tipo)
            return self._expressao.get_tipo(ambiente)
        finally:
            ambiente.restaura()

    def get_seqdec_funcional(self) -> list[DeclaracaoFuncional]:
        return self._seqdec_funcional

    def get_expressao(self) -> Expressao:
        return self._expressao
