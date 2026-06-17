from __future__ import annotations

from typing import Any

from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.functional1.declaration.declaracao_funcional import DeclaracaoFuncional


class DecVariavel(DeclaracaoFuncional):
    def __init__(self, id_arg: Id, expressao_arg: Expressao) -> None:
        self._id = id_arg
        self._expressao = expressao_arg

    def get_aridade(self) -> int:
        return 0

    def __str__(self) -> str:
        return f"var {self._id} = {self._expressao}"

    def get_expressao(self) -> Expressao:
        return self._expressao

    def get_id(self) -> Id:
        return self._id

    def get_tipo(self, amb: Any) -> Any:
        return self._expressao.get_tipo(amb)

    def checa_tipo(self, ambiente: Any) -> bool:
        return self._expressao.checa_tipo(ambiente)
