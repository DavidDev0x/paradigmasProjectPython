from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression.exp_binaria import ExpBinaria
from li2.plp.expressions2.expression.valor_booleano import ValorBooleano
from li2.plp.expressions2.expression.valor_concreto import ValorConcreto
from li2.plp.expressions2.memory.erro_tipo_expressao_exception import ErroTipoExpressaoException


class ExpEquals(ExpBinaria):
    def __init__(self, esq, dir) -> None:
        super().__init__(esq, dir, "==")

    def avaliar(self, ambiente):
        esq = self.get_esq().avaliar(ambiente)
        dir = self.get_dir().avaliar(ambiente)
        if not isinstance(esq, ValorConcreto) or not isinstance(dir, ValorConcreto):
            raise ErroTipoExpressaoException("O operador == exige valores concretos.")
        if type(esq) is not type(dir):
            raise ErroTipoExpressaoException(
                f"O operador == exige operandos do mesmo tipo: {type(esq).__name__} e {type(dir).__name__}."
            )
        return ValorBooleano(esq.is_equals(dir))

    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.get_esq().get_tipo(ambiente).e_igual(self.get_dir().get_tipo(ambiente))

    def get_tipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self):
        return ExpEquals(self.get_esq().clone(), self.get_dir().clone())
