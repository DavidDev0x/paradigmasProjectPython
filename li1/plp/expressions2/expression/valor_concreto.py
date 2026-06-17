from __future__ import annotations
from abc import abstractmethod
from typing import Any, TYPE_CHECKING
from .valor import Valor
if TYPE_CHECKING:
    from li1.plp.expressions1.util.tipo import Tipo
    from li1.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from li1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao

class ValorConcreto(Valor):
    """Classe abstrata para valores primitivos concretos."""

    def __init__(self, valor: Any) -> None:
        self._valor = valor

    def __str__(self) -> str:
        return str(self._valor)

    def valor(self) -> Any:
        return self._valor

    def is_equals(self, obj: 'ValorConcreto') -> bool:
        return self.valor() == obj.valor()

    def avaliar(self, amb: 'AmbienteExecucao | None') -> 'Valor':
        return self

    def checa_tipo(self, amb: 'AmbienteCompilacao | None') -> bool:
        return True

    def __hash__(self) -> int:
        return hash((type(self), self._valor))

    def __eq__(self, obj: object) -> bool:
        return type(self) is type(obj) and isinstance(obj, ValorConcreto) and self._valor == obj._valor

    def reduzir(self, ambiente: 'AmbienteExecucao') -> 'ValorConcreto':
        return self

    @abstractmethod
    def get_tipo(self, amb: 'AmbienteCompilacao | None') -> 'Tipo': ...

    @abstractmethod
    def clone(self) -> 'ValorConcreto': ...
