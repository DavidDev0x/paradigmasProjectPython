from __future__ import annotations

from typing import Any

from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.expressions2.expression.valor import Valor
from lf1.plp.functional1.memory.ambiente_execucao_funcional import AmbienteExecucaoFuncional


class Aplicacao(Expressao):
    def __init__(self, f: Id, expressoes: list[Expressao]) -> None:
        self._func = f
        self._args_expressao = list(expressoes)

    def __str__(self) -> str:
        args = ", ".join(str(exp) for exp in self._args_expressao)
        return f"{self._func}({args})"

    def avaliar(self, ambiente: Any) -> Valor:
        if not isinstance(ambiente, AmbienteExecucaoFuncional):
            raise TypeError("Aplicacao exige AmbienteExecucaoFuncional.")
        funcao = ambiente.get_funcao(self._func)
        map_id_valor = self.resolve_parameters_bindings(ambiente, funcao)
        ambiente.incrementa()
        try:
            self.include_value_bindings(ambiente, map_id_valor)
            return funcao.get_exp().avaliar(ambiente)
        finally:
            ambiente.restaura()

    def include_value_bindings(self, ambiente: Any, map_id_valor: dict[Id, Valor]) -> None:
        for id_arg, valor in map_id_valor.items():
            ambiente.map(id_arg, valor)

    def resolve_parameters_bindings(self, ambiente: Any, funcao: Any) -> dict[Id, Valor]:
        parametros_id = funcao.get_lista_id()
        if len(parametros_id) != len(self._args_expressao):
            raise TypeError(f"Função {self._func} esperava {len(parametros_id)} argumento(s), recebeu {len(self._args_expressao)}.")
        map_id_valor: dict[Id, Valor] = {}
        for id_arg, exp in zip(parametros_id, self._args_expressao):
            map_id_valor[id_arg] = exp.avaliar(ambiente)
        return map_id_valor

    def checa_tipo(self, ambiente: Any) -> bool:
        tipo_funcao = ambiente.get(self._func)
        return self.check_argument_list_size(tipo_funcao) and self.check_argument_types(ambiente, tipo_funcao)

    def check_argument_types(self, ambiente: Any, tipo_funcao: Any) -> bool:
        tipo_atual = tipo_funcao
        for valor_real in self._args_expressao:
            if not valor_real.checa_tipo(ambiente):
                return False
            tipo_arg = valor_real.get_tipo(ambiente)
            if tipo_arg.intersecao(tipo_atual).e_void():
                return False
            tipo_atual = tipo_atual.get_prox()
            if tipo_atual is None:
                return False
        return True

    def check_argument_list_size(self, tipo_funcao: Any) -> bool:
        tamanho_tipo = 0
        aux = tipo_funcao
        while aux is not None:
            tamanho_tipo += 1
            aux = aux.get_prox()
        return (tamanho_tipo - 1) == len(self._args_expressao)

    def get_tipo(self, ambiente: Any) -> Any:
        tipo = ambiente.get(self._func)
        for _ in self._args_expressao:
            if tipo.get_prox() is None:
                break
            tipo = tipo.get_prox()
        return tipo

    def get_func(self) -> Id:
        return self._func

    def get_args_expressao(self) -> list[Expressao]:
        return self._args_expressao
