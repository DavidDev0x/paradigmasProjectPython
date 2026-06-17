from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_binaria import ExpBinaria
from .expressao import Expressao
from .valor_booleano import ValorBooleano
from ._type_helpers import require_booleano

class ExpOr(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, 'or')

    def avaliar(self, amb):
        return ValorBooleano(require_booleano(self.get_esq().avaliar(amb)).valor() or require_booleano(self.get_dir().avaliar(amb)).valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_booleano() and self.get_dir().get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ExpOr':
        return ExpOr(self.esq.clone(), self.dir.clone())
