from __future__ import annotations
from li1.plp.imperative1.declaration.declaracao import Declaracao
from .comando import Comando

class ComandoDeclaracao(Comando):
    def __init__(self, declaracao: Declaracao, comando: Comando) -> None:
        self._declaracao = declaracao
        self._comando = comando

    def executar(self, ambiente):
        ambiente.incrementa()
        try:
            ambiente = self._comando.executar(self._declaracao.elabora(ambiente))
        finally:
            ambiente.restaura()
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        ambiente.incrementa()
        try:
            return self._declaracao.checa_tipo(ambiente) and self._comando.checa_tipo(ambiente)
        finally:
            ambiente.restaura()
