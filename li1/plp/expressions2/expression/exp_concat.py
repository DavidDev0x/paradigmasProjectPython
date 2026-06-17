from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .exp_binaria import ExpBinaria
from .expressao import Expressao
from .valor_string import ValorString
from ._type_helpers import require_string

class ExpConcat(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, '++')

    def avaliar(self, amb):
        return ValorString(require_string(self.get_esq().avaliar(amb)).valor() + require_string(self.get_dir().avaliar(amb)).valor())

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_string() and self.get_dir().get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente) -> TipoPrimitivo:
        return TipoPrimitivo.STRING

    def clone(self) -> 'ExpConcat':
        return ExpConcat(self.esq.clone(), self.dir.clone())
