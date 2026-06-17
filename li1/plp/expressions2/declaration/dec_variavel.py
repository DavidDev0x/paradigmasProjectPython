from li1.plp.expressions2.expression.expressao import Expressao
from li1.plp.expressions2.expression.id import Id

class DecVariavel:
    def __init__(self, id_arg: Id, expressao_arg: Expressao) -> None:
        self._id = id_arg
        self._expressao = expressao_arg

    def get_id(self) -> Id:
        return self._id

    def get_expressao(self) -> Expressao:
        return self._expressao
