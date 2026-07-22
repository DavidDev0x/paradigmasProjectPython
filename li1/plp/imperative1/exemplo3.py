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

class Exemplo3:
    def criar_programa(self) -> Programa:
        i = Id('i')
        return Programa(ComandoDeclaracao(
            DeclaracaoVariavel(i, ValorInteiro(0)),
            While(
                ExpNot(ExpEquals(i, ValorInteiro(3))),
                SequenciaComando(
                    Atribuicao(i, ExpSoma(i, ValorInteiro(1))),
                    Write(ValorString('Hello World'))
                )
            )
        ))

    def main(self) -> str:
        programa = self.criar_programa()
        if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
            return str(programa.executar(ContextoExecucaoImperativa(None)))
        return 'Erro de tipo: o programa Exemplo3 nao passou na checagem de tipos.'


if __name__ == '__main__':
    exemplo = Exemplo3()
    print(exemplo.main())
