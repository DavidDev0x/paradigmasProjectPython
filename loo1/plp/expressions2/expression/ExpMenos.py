from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException
from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from .ExpUnaria import ExpUnaria
from .ValorInteiro import ValorInteiro


class ExpMenos(ExpUnaria):
    def __init__(self, exp):
        super().__init__(exp, "-")

    def avaliar(self, ambiente):
        valor = self.get_exp().avaliar(ambiente)
        if not isinstance(valor, ValorInteiro):
            raise ErroTipoException("O operador unário '-' exige um valor inteiro.")
        return ValorInteiro(-valor.valor())

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_exp().get_tipo(ambiente).e_inteiro()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self):
        return ExpMenos(self._exp.clone())
