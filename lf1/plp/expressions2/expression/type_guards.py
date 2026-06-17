from lf1.plp.expressions2.expression.valor_booleano import ValorBooleano
from lf1.plp.expressions2.expression.valor_concreto import ValorConcreto
from lf1.plp.expressions2.expression.valor_inteiro import ValorInteiro
from lf1.plp.expressions2.expression.valor_string import ValorString


def ensure_inteiro(valor: object, operador: str) -> ValorInteiro:
    if not isinstance(valor, ValorInteiro):
        raise TypeError(f"Operador {operador} exige ValorInteiro; recebeu {type(valor).__name__}.")
    return valor


def ensure_booleano(valor: object, operador: str) -> ValorBooleano:
    if not isinstance(valor, ValorBooleano):
        raise TypeError(f"Operador {operador} exige ValorBooleano; recebeu {type(valor).__name__}.")
    return valor


def ensure_string(valor: object, operador: str) -> ValorString:
    if not isinstance(valor, ValorString):
        raise TypeError(f"Operador {operador} exige ValorString; recebeu {type(valor).__name__}.")
    return valor


def ensure_concreto(valor: object, operador: str) -> ValorConcreto:
    if not isinstance(valor, ValorConcreto):
        raise TypeError(f"Operador {operador} exige ValorConcreto; recebeu {type(valor).__name__}.")
    return valor
