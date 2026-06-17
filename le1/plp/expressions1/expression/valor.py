from __future__ import annotations

from abc import ABC

from le1.plp.expressions1.expression.expressao import Expressao


class Valor(Expressao, ABC):
    """Agrupa valores concretos e abstratos."""
