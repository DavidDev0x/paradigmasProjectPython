from .valor_inteiro import ValorInteiro
from .valor_booleano import ValorBooleano
from .valor_string import ValorString
from .valor_concreto import ValorConcreto

def require_inteiro(valor: object) -> ValorInteiro:
    if not isinstance(valor, ValorInteiro):
        raise TypeError(f'Esperado ValorInteiro, recebido {type(valor).__name__}.')
    return valor

def require_booleano(valor: object) -> ValorBooleano:
    if not isinstance(valor, ValorBooleano):
        raise TypeError(f'Esperado ValorBooleano, recebido {type(valor).__name__}.')
    return valor

def require_string(valor: object) -> ValorString:
    if not isinstance(valor, ValorString):
        raise TypeError(f'Esperado ValorString, recebido {type(valor).__name__}.')
    return valor

def require_concreto(valor: object) -> ValorConcreto:
    if not isinstance(valor, ValorConcreto):
        raise TypeError(f'Esperado ValorConcreto, recebido {type(valor).__name__}.')
    return valor
