from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_unaria import ExpUnaria
from .expressao import Expressao
from .valor_inteiro import ValorInteiro
from ._type_helpers import require_inteiro

class ExpMenos(ExpUnaria):
    def __init__(self, exp: Expressao) -> None:
        super().__init__(exp, '-')

    def avaliar(self, amb):
        return ValorInteiro(-require_inteiro(self.get_exp().avaliar(amb)).valor())

    def checa_tipo_elemento_terminal(self, amb) -> bool:
        return self.get_exp().get_tipo(amb).e_inteiro()

    def get_tipo(self, amb) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ExpMenos':
        return ExpMenos(self.exp.clone())
