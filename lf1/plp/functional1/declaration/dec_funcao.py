from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.functional1.declaration.declaracao_funcional import DeclaracaoFuncional
from lf1.plp.functional1.util.valor_funcao import ValorFuncao


class DecFuncao(DeclaracaoFuncional):
    def __init__(self, id_fun: Id, valor_funcao: ValorFuncao) -> None:
        self._id = id_fun
        self._valor_funcao = valor_funcao

    def __str__(self) -> str:
        parametros = ", ".join(str(id_arg) for id_arg in self._valor_funcao.get_lista_id())
        return f"fun {self._id} ({parametros}) = {self._valor_funcao.get_exp()}"

    def get_id(self) -> Id:
        return self._id

    def get_expressao(self) -> Any:
        return self._valor_funcao.get_exp()

    def get_funcao(self) -> ValorFuncao:
        return self._valor_funcao

    def get_aridade(self) -> int:
        return self._valor_funcao.get_aridade()

    def checa_tipo(self, ambiente: Any) -> bool:
        ambiente.incrementa()
        try:
            tipo = Tipo()
            for _ in range(self.get_aridade() - 1, -1, -1):
                tipo = Tipo(tipo)
            ambiente.map(self._id, tipo)
            return self._valor_funcao.checa_tipo(ambiente)
        finally:
            ambiente.restaura()

    def get_tipo(self, amb: Any) -> Tipo:
        amb.incrementa()
        try:
            tipo = Tipo()
            for _ in range(self.get_aridade() - 1, -1, -1):
                tipo = Tipo(tipo)
            amb.map(self._id, tipo)
            return self._valor_funcao.get_tipo(amb)
        finally:
            amb.restaura()
