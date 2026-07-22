from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException
from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from .ExpUnaria import ExpUnaria
from .ValorString import ValorString
from .ValorInteiro import ValorInteiro


class ExpLength(ExpUnaria):
    def __init__(self, exp):
        super().__init__(exp, "length")

    def avaliar(self, ambiente):
        valor = self.get_exp().avaliar(ambiente)
        if not isinstance(valor, ValorString):
            raise ErroTipoException("O operador 'length' exige uma string.")
        return ValorInteiro(len(valor.valor()))

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_exp().get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self):
        return ExpLength(self._exp.clone())
