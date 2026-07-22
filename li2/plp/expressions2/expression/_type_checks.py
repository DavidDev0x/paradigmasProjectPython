from li2.plp.expressions2.memory.erro_tipo_expressao_exception import ErroTipoExpressaoException


def exigir_tipo(valor, classe, operador: str):
    if type(valor) is not classe:
        raise ErroTipoExpressaoException(
            f"Operador {operador}: esperado {classe.__name__}, recebido {type(valor).__name__}."
        )
    return valor
