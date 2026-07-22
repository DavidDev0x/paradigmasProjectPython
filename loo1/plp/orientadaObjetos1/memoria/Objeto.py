from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class Objeto:
    def __init__(self, classe_objeto, estado_obj):
        self._classe_objeto = classe_objeto
        self._estado = estado_obj

    def get_classe(self):
        return self._classe_objeto

    def get_estado(self):
        return self._estado

    def set_estado(self, novo_estado) -> None:
        self._estado = novo_estado

    def map_this(self, referencia) -> None:
        identificador = Id("this")
        self._estado.remove(identificador)
        self._estado.put(identificador, referencia)

    def change_atributo(self, id_variavel, valor) -> None:
        if not self._estado.contains_key(id_variavel):
            raise VariavelNaoDeclaradaException(id_variavel)
        self._estado.put(id_variavel, valor)

    def __repr__(self) -> str:
        return f"Objeto(classe={self._classe_objeto!s}, estado={self._estado.as_dict()!r})"
