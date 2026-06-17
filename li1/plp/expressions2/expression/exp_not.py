from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_unaria import ExpUnaria
from .expressao import Expressao
from .valor_booleano import ValorBooleano
from ._type_helpers import require_booleano

class ExpNot(ExpUnaria):
    def __init__(self, exp: Expressao) -> None:
        super().__init__(exp, '~')

    def avaliar(self, amb):
        return ValorBooleano(not require_booleano(self.get_exp().avaliar(amb)).valor())

    def checa_tipo_elemento_terminal(self, amb) -> bool:
        return self.get_exp().get_tipo(amb).e_booleano()

    def get_tipo(self, amb) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ExpNot':
        return ExpNot(self.exp.clone())
