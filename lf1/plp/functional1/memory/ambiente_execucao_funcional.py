from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from lf1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class AmbienteExecucaoFuncional(AmbienteExecucao, ABC):
    @abstractmethod
    def map_funcao(self, id_arg: Any, funcao: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_funcao(self, id_arg: Any) -> Any:
        raise NotImplementedError
