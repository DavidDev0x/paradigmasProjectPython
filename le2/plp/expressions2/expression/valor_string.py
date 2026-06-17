from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression.valor_concreto import ValorConcreto
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao


class ValorString(ValorConcreto):
    def __init__(self, valor: str) -> None:
        if type(valor) is not str:
            raise TypeError("ValorString exige str.")
        super().__init__(valor)

    def valor(self) -> str:
        return self._valor

    def get_tipo(self, amb: AmbienteCompilacao) -> Tipo:
        return Tipo.TIPO_STRING
