from abc import ABC
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class ExpBinaria(Expressao, ABC):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str):
        self._esq = esq
        self._dir = dir
        self._operador = operador

    def get_esq(self) -> Expressao:
        return self._esq

    def get_dir(self) -> Expressao:
        return self._dir

    def get_operador(self) -> str:
        return self._operador

    def checa_tipo(self, ambiente) -> bool:
        return self._esq.checa_tipo(ambiente) and self._dir.checa_tipo(ambiente)
