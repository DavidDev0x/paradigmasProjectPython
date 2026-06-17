from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression.valor_concreto import ValorConcreto
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool) -> None:
        if type(valor) is not bool:
            raise TypeError("ValorBooleano exige bool.")
        super().__init__(valor)

    def valor(self) -> bool:
        return self._valor

    def get_tipo(self, amb: AmbienteCompilacao) -> Tipo:
        return Tipo.TIPO_BOOLEANO
