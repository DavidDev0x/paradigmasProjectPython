from __future__ import annotations

from typing import TYPE_CHECKING

from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.valor import Valor

if TYPE_CHECKING:
    from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class Id(Expressao):
    def __init__(self, str_name: str) -> None:
        if type(str_name) is not str:
            raise TypeError("Id exige uma string como nome.")
        self._id_name = str_name

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, Id) and obj._id_name == self._id_name

    def __hash__(self) -> int:
        return hash(self._id_name)

    def __str__(self) -> str:
        return self._id_name

    def avaliar(self, ambiente: AmbienteExecucao) -> Valor:
        valor = ambiente.get(self)
        if not isinstance(valor, Valor):
            raise TypeError("Ambiente de execução retornou objeto que não implementa Valor.")
        return valor

    def checa_tipo(self, amb: AmbienteCompilacao) -> bool:
        amb.get(self)
        return True

    def get_tipo(self, amb: AmbienteCompilacao) -> Tipo:
        tipo = amb.get(self)
        if not isinstance(tipo, Tipo):
            raise TypeError("Ambiente de compilação retornou objeto que não é Tipo.")
        return tipo

    def get_id_name(self) -> str:
        return self._id_name

    def set_id_name(self, id_name: str) -> None:
        if type(id_name) is not str:
            raise TypeError("id_name deve ser string.")
        self._id_name = id_name
