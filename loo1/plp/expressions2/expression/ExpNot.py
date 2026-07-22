from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException
from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from .ExpUnaria import ExpUnaria
from .ValorBooleano import ValorBooleano


class ExpNot(ExpUnaria):
    def __init__(self, exp):
        super().__init__(exp, "not")

    def avaliar(self, ambiente):
        valor = self.get_exp().avaliar(ambiente)
        if not isinstance(valor, ValorBooleano):
            raise ErroTipoException("O operador 'not' exige um valor booleano.")
        return ValorBooleano(not valor.valor())

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_exp().get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self):
        return ExpNot(self._exp.clone())
