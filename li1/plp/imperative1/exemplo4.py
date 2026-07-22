from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from li1.plp.expressions2.expression import *
from li1.plp.expressions2.memory import (
    IdentificadorJaDeclaradoException,
    IdentificadorNaoDeclaradoException,
    VariavelJaDeclaradaException,
    VariavelNaoDeclaradaException,
)
from li1.plp.imperative1.command import *
from li1.plp.imperative1.declaration import *
from li1.plp.imperative1.memory import (
    ContextoCompilacaoImperativa,
    ContextoExecucaoImperativa,
    EntradaVaziaException,
    ErroTipoEntradaException,
)
from li1.plp.imperative1.programa import Programa


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

    def _tratar_erro(self, tipo: str, erro: Exception) -> str:
        return f'{tipo}: {type(erro).__name__}: {erro}'

    def _executar_com_tratamento(self, programa: Programa) -> str:
        try:
            if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
                return str(programa.executar(ContextoExecucaoImperativa(None)))
            return f'Erro de tipo: o programa {type(self).__name__} nao passou na checagem de tipos.'
        except VariavelJaDeclaradaException as erro:
            return self._tratar_erro('Variavel ja declarada', erro)
        except VariavelNaoDeclaradaException as erro:
            return self._tratar_erro('Variavel nao declarada', erro)
        except IdentificadorJaDeclaradoException as erro:
            return self._tratar_erro('Identificador ja declarado', erro)
        except IdentificadorNaoDeclaradoException as erro:
            return self._tratar_erro('Identificador nao declarado', erro)
        except EntradaVaziaException as erro:
            return self._tratar_erro('Entrada vazia', erro)
        except ErroTipoEntradaException as erro:
            return self._tratar_erro('Erro de tipo na entrada', erro)
        except TypeError as erro:
            return self._tratar_erro('Erro de tipo', erro)
        except RuntimeError as erro:
            return self._tratar_erro('Erro de execucao', erro)
        except Exception as erro:
            return self._tratar_erro('Erro inesperado', erro)

    def main(self) -> str:
        programa = self.criar_programa()
        return self._executar_com_tratamento(programa)


if __name__ == '__main__':
    exemplo = Exemplo4()
    print(exemplo.main())
