from __future__ import annotations
from typing import TYPE_CHECKING
from .expressao import Expressao
from li1.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
if TYPE_CHECKING:
    from li1.plp.expressions1.util.tipo import Tipo
    from li1.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from li1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao
    from .valor import Valor

class Id(Expressao):
    def __init__(self, str_name: str) -> None:
        if type(str_name) is not str or not str_name:
            raise TypeError('Id exige uma string não vazia.')
        self._id_name = str_name

    def __str__(self) -> str:
        return self._id_name

    def avaliar(self, ambiente: 'AmbienteExecucao') -> 'Valor':
        return ambiente.get(self)

    def checa_tipo(self, amb: 'AmbienteCompilacao') -> bool:
        amb.get(self)
        return True

    def get_tipo(self, amb: 'AmbienteCompilacao') -> 'Tipo':
        return amb.get(self)

    def get_id_name(self) -> str:
        return self._id_name

    def set_id_name(self, id_name: str) -> None:
        if type(id_name) is not str or not id_name:
            raise TypeError('Id exige uma string não vazia.')
        self._id_name = id_name

    def __hash__(self) -> int:
        return hash(self._id_name)

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, Id) and self._id_name == obj._id_name

    def reduzir(self, ambiente: 'AmbienteExecucao') -> Expressao:
        try:
            valor = ambiente.get(self)
            return valor.clone()
        except VariavelNaoDeclaradaException:
            return self

    def clone(self) -> 'Id':
        return self
