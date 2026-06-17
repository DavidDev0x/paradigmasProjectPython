from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_binaria import ExpBinaria
from .expressao import Expressao
from .valor_booleano import ValorBooleano
from ._type_helpers import require_concreto

class ExpEquals(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, '==')

    def avaliar(self, amb):
        esq = require_concreto(self.get_esq().avaliar(amb))
        dir = require_concreto(self.get_dir().avaliar(amb))
        return ValorBooleano(esq.is_equals(dir))

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_igual(self.get_dir().get_tipo(ambiente))

    def get_tipo(self, ambiente) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ExpEquals':
        return ExpEquals(self.esq.clone(), self.dir.clone())
