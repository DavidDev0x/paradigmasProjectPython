from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    tipo: str
    texto: str
    posicao: int
