from .DecClasse import DecClasse
from loo1.plp.orientadaObjetos1.memoria.DefClasse import DefClasse
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class DecClasseSimples(DecClasse):
    def __init__(self, nome_classe, atributos, metodos):
        self._nome_classe = nome_classe
        self._atributos = atributos
        self._metodos = metodos

    def checa_tipo(self, ambiente) -> bool:
        ambiente.map_def_classe(
            self._nome_classe,
            DefClasse(self._nome_classe, self._atributos, self._metodos),
        )
        ambiente.incrementa()
        try:
            if not self._atributos.checa_tipo(ambiente):
                return False
            ambiente.map(Id("this"), TipoClasse(self._nome_classe))
            return self._metodos.checa_tipo(ambiente)
        finally:
            ambiente.restaura()

    def elabora(self, ambiente):
        ambiente.map_def_classe(
            self._nome_classe,
            DefClasse(self._nome_classe, self._atributos, self._metodos),
        )
        return ambiente
