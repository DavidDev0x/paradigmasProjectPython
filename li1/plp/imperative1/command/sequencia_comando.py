from __future__ import annotations
from .comando import Comando

class SequenciaComando(Comando):
    def __init__(self, comando1: Comando, comando2: Comando) -> None:
        self._comando1 = comando1
        self._comando2 = comando2

    def executar(self, ambiente):
        return self._comando2.executar(self._comando1.executar(ambiente))

    def checa_tipo(self, ambiente) -> bool:
        return self._comando1.checa_tipo(ambiente) and self._comando2.checa_tipo(ambiente)
