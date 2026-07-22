from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.id import Id


class DecVariavel:
    def __init__(self, id_arg: Id, expressao_arg: Expressao) -> None:
        if not isinstance(id_arg, Id):
            raise TypeError("id_arg deve ser Id.")
        if not isinstance(expressao_arg, Expressao):
            raise TypeError("expressao_arg deve implementar Expressao.")
        self._id = id_arg
        self._expressao = expressao_arg

    def get_id(self) -> Id:
        return self._id

    def get_expressao(self) -> Expressao:
        return self._expressao

    def __str__(self) -> str:
        return f"var {self._id} = {self._expressao}"
