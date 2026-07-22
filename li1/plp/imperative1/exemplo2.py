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

class Exemplo2:
    def criar_programa(self) -> Programa:
        a_externo = Id('a')
        a_interno = Id('a')
        b = Id('b')

        bloco_interno = ComandoDeclaracao(
            DeclaracaoComposta(
                DeclaracaoVariavel(a_interno, ValorInteiro(2)),
                DeclaracaoVariavel(b, ValorInteiro(5))
            ),
            SequenciaComando(
                Write(a_interno),
                Write(ExpSoma(b, a_interno))
            )
        )

        return Programa(ComandoDeclaracao(
            DeclaracaoVariavel(a_externo, ValorInteiro(3)),
            SequenciaComando(
                Write(a_externo),
                SequenciaComando(bloco_interno, Write(a_externo))
            )
        ))

    def main(self) -> str:
        programa = self.criar_programa()
        if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
            return str(programa.executar(ContextoExecucaoImperativa(None)))
        return 'Erro de tipo: o programa Exemplo2 nao passou na checagem de tipos.'


if __name__ == '__main__':
    exemplo = Exemplo2()
    print(exemplo.main())
