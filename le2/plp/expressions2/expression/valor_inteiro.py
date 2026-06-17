from le2.plp.expressions1.util.tipo import Tipo
from le2.plp.expressions2.expression.valor_concreto import ValorConcreto
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int) -> None:
        if type(valor) is not int:
            raise TypeError("ValorInteiro exige int puro; bool não é aceito como inteiro.")
        super().__init__(valor)

    def valor(self) -> int:
        return self._valor

    def get_tipo(self, amb: AmbienteCompilacao) -> Tipo:
        return Tipo.TIPO_INTEIRO
