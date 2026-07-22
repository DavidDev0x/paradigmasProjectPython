from .DecVariavel import DecVariavel
from .SimplesDecVariavel import SimplesDecVariavel
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class DecVariavelObjeto(DecVariavel):
    def __init__(self, tipo, objeto, classe):
        self._tipo = tipo
        self._objeto = objeto
        self._classe = classe

    def get_tipo(self, identificador=None):
        if identificador is None:
            return self._tipo
        if self._objeto == identificador:
            return self._tipo
        raise VariavelNaoDeclaradaException(identificador)

    def elabora(self, ambiente):
        from loo1.plp.orientadaObjetos1.comando.New import New
        SimplesDecVariavel(self._tipo, self._objeto, ValorNull()).elabora(ambiente)
        return New(self._objeto, self._classe).executar(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        tipo_classe = TipoClasse(self._classe)
        resposta = tipo_classe.e_valido(ambiente) and self._tipo.e_valido(ambiente) and tipo_classe == self._tipo
        if resposta:
            ambiente.map(self._objeto, tipo_classe)
        return resposta

    def get_objeto(self):
        return self._objeto

    def get_classe(self):
        return self._classe
