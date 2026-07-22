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

class Exemplo4:
    def criar_programa(self) -> Programa:
        n = Id('n')
        m = Id('n')
        return Programa(ComandoDeclaracao(
            DeclaracaoComposta(
                DeclaracaoVariavel(n, ValorInteiro(0)),
                DeclaracaoVariavel(m, ValorInteiro(0))
            ),
            SequenciaComando(
                Atribuicao(n, ValorInteiro(2)),
                SequenciaComando(
                    Atribuicao(m, ValorInteiro(3)),
                    IfThenElse(
                        ExpEquals(m, n),
                        Write(ValorString('valores de entrada iguais')),
                        Write(ValorString('valores de entrada diferentes'))
                    )
                )
            )
        ))

    def main(self) -> str:
        programa = self.criar_programa()
        try:
            if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
                return str(programa.executar(ContextoExecucaoImperativa(None)))
            return 'Erro de tipo: o programa Exemplo4 nao passou na checagem de tipos.'
        except Exception as exc:
            return f'Erro esperado em Exemplo4: {type(exc).__name__}: {exc}'


if __name__ == '__main__':
    exemplo = Exemplo4()
    print(exemplo.main())
