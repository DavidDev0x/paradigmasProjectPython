from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from li1.plp.expressions2.expression import *
from li1.plp.imperative1.programa import Programa
from li1.plp.imperative1.command import *
from li1.plp.imperative1.declaration import *
from li1.plp.imperative1.memory import *

class Exemplo1:
    def criar_programa(self) -> Programa:
        a = Id('3')
        return Programa(ComandoDeclaracao(DeclaracaoVariavel(a, ValorInteiro(3)), Write(a)))

    def main(self) -> str:
        programa = self.criar_programa()
        if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
            return str(programa.executar(ContextoExecucaoImperativa(None)))
        return 'Erro de tipo: o programa Exemplo1 nao passou na checagem de tipos.'


if __name__ == '__main__':
    exemplo = Exemplo1()
    print(exemplo.main())
