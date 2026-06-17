from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_unaria import ExpUnaria
from .expressao import Expressao
from .valor_inteiro import ValorInteiro
from ._type_helpers import require_string

class ExpLength(ExpUnaria):
    def __init__(self, exp: Expressao) -> None:
        super().__init__(exp, 'length')

    def avaliar(self, amb):
        return ValorInteiro(len(require_string(self.get_exp().avaliar(amb)).valor()))

    def checa_tipo_elemento_terminal(self, amb) -> bool:
        return self.get_exp().get_tipo(amb).e_string()

    def get_tipo(self, amb) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ExpLength':
        return ExpLength(self.exp.clone())
