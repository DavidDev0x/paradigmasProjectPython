from .Tipo import Tipo


class TipoClasse(Tipo):
    def __init__(self, tipo_classe):
        self._tipo_classe = tipo_classe

    def get_tipo(self):
        return self._tipo_classe

    def e_valido(self, ambiente) -> bool:
        if self == TipoClasse.TIPO_NULL:
            return True
        try:
            return ambiente.get_def_classe(self._tipo_classe) is not None
        except Exception:
            return False

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, TipoClasse) and self._tipo_classe == outro._tipo_classe

    def __hash__(self) -> int:
        return hash((TipoClasse, self._tipo_classe))

    def __str__(self) -> str:
        return str(self._tipo_classe)


from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
TipoClasse.NULL = Id("NULL")
TipoClasse.TIPO_NULL = TipoClasse(TipoClasse.NULL)
