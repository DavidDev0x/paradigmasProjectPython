from le2.plp.expressions2.memory.tipo_invalido_exception import TipoInvalidoException


def exigir(valor: object, classe: type, esperado: str, operador: str) -> object:
    if not isinstance(valor, classe):
        raise TipoInvalidoException(esperado, valor, operador)
    return valor
