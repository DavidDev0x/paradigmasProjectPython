from .IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException
from .IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class StackHandler:
    @staticmethod
    def get_from_id(stack: list[dict], identificador):
        for mapa in reversed(stack):
            if identificador in mapa and mapa[identificador] is not None:
                return mapa[identificador]
        raise IdentificadorNaoDeclaradoException()

    @staticmethod
    def map_id_object(stack: list[dict], identificador, objeto) -> None:
        if not stack:
            raise RuntimeError("Pilha de escopos vazia.")
        if identificador in stack[-1]:
            raise IdentificadorJaDeclaradoException()
        stack[-1][identificador] = objeto
