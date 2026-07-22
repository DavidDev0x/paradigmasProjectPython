from .DecVariavel import DecVariavel
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class CompostaDecVariavel(DecVariavel):
    def __init__(self, declaracao1, declaracao2):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def get_tipo(self, identificador):
        try:
            return self._declaracao1.get_tipo(identificador)
        except VariavelNaoDeclaradaException:
            return self._declaracao2.get_tipo(identificador)

    def elabora(self, ambiente):
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checa_tipo(self, ambiente) -> bool:
        return self._declaracao1.checa_tipo(ambiente) and self._declaracao2.checa_tipo(ambiente)
