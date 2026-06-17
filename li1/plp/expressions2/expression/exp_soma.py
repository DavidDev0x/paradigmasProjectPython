from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_binaria import ExpBinaria
from .expressao import Expressao
from .valor_inteiro import ValorInteiro
from ._type_helpers import require_inteiro

class ExpSoma(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, '+')

    def avaliar(self, amb):
        return ValorInteiro(require_inteiro(self.get_esq().avaliar(amb)).valor() + require_inteiro(self.get_dir().avaliar(amb)).valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_inteiro() and self.get_dir().get_tipo(ambiente).e_inteiro()

    def get_tipo(self, ambiente) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ExpSoma':
        return ExpSoma(self.esq.clone(), self.dir.clone())
