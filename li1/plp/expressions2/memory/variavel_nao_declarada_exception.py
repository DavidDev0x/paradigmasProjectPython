from __future__ import annotations
from .identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException

class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id_arg: object) -> None:
        super().__init__(f'Variável {id_arg} não declarada.')
