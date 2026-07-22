from .Tipo import Tipo


class TipoPrimitivo(Tipo):
    INTEIRO = 1
    BOOLEANO = 2
    STRING = 4

    def __init__(self, tipo: int):
        self._tipo = tipo

    def get_tipo(self):
        from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
        nomes = {
            self.INTEIRO: "int",
            self.BOOLEANO: "boolean",
            self.STRING: "string",
        }
        return Id(nomes.get(self._tipo, "undefined"))

    def e_inteiro(self) -> bool:
        return self._tipo == self.INTEIRO

    def e_booleano(self) -> bool:
        return self._tipo == self.BOOLEANO

    def e_string(self) -> bool:
        return self._tipo == self.STRING

    def e_valido(self, ambiente=None) -> bool:
        return self._tipo in {self.INTEIRO, self.BOOLEANO, self.STRING}

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, TipoPrimitivo) and self._tipo == outro._tipo

    def __hash__(self) -> int:
        return hash((TipoPrimitivo, self._tipo))

    def __str__(self) -> str:
        return {
            self.INTEIRO: "int",
            self.BOOLEANO: "boolean",
            self.STRING: "string",
        }.get(self._tipo, "undefined")


TipoPrimitivo.TIPO_INTEIRO = TipoPrimitivo(TipoPrimitivo.INTEIRO)
TipoPrimitivo.TIPO_BOOLEANO = TipoPrimitivo(TipoPrimitivo.BOOLEANO)
TipoPrimitivo.TIPO_STRING = TipoPrimitivo(TipoPrimitivo.STRING)
