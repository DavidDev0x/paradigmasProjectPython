from pathlib import Path
import sys
from typing import Optional

if __package__ is None or __package__ == "":
    project_root = Path(__file__).resolve().parents[3]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from le2.plp.expressions2.programa import Programa
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import ExpDeclaracao, ExpSoma, Id, ValorInteiro
from le2.plp.expressions2.memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException
from le2.plp.expressions2.memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException
from le2.plp.expressions2.memory.tipo_invalido_exception import TipoInvalidoException
from le2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from le2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException


def executar_com_tratamento(programa: Programa) -> tuple[bool, str]:
    try:
        tipo_valido = programa.checa_tipo()
        if tipo_valido:
            return True, str(programa.executar())
        return False, "Erro de tipo: a expressão não passou na checagem de tipos."
    except VariavelJaDeclaradaException as erro:
        return False, f"Erro de variável já declarada: {erro}"
    except VariavelNaoDeclaradaException as erro:
        return False, f"Erro de variável não declarada: {erro}"
    except IdentificadorJaDeclaradoException as erro:
        return False, f"Erro de identificador já declarado: {erro}"
    except IdentificadorNaoDeclaradoException as erro:
        return False, f"Erro de identificador não declarado: {erro}"
    except TipoInvalidoException as erro:
        return False, f"Erro de tipo inválido: {erro}"
    except TypeError as erro:
        return False, f"Erro de tipo: {erro}"
    except RuntimeError as erro:
        return False, f"Erro de execução: {erro}"
    except Exception as erro:
        return False, f"Erro inesperado: {erro}"


def imprimir_execucao(programa: Programa, tipo_valido: bool, mensagem: str) -> None:
    print(f"Expressao: {programa.get_expressao()}")
    print(f"Tipo valido: {tipo_valido}")
    if tipo_valido:
        print(f"Resultado: {mensagem}")
    else:
        print(mensagem)

class Exemplo5:
    @staticmethod
    def criar_programa() -> Programa:
        dec_y = DecVariavel(Id("y"), Id("x"))
        corpo_mais_interno = ExpSoma(Id("x"), Id("y"))
        let_y = ExpDeclaracao([dec_y], corpo_mais_interno)

        dec_x_4 = DecVariavel(Id("x"), ExpSoma(Id("x"), ValorInteiro(1)))
        let_x_4 = ExpDeclaracao([dec_x_4], let_y)

        dec_x_3 = DecVariavel(Id("x"), ValorInteiro(3))
        let_x_3 = ExpDeclaracao([dec_x_3], let_x_4)
        return Programa(let_x_3)

    @staticmethod
    def executar(programa: Optional[Programa] = None) -> tuple[bool, str]:
        if programa is None:
            programa = Exemplo5.criar_programa()
        return executar_com_tratamento(programa)


if __name__ == "__main__":
    programa = Exemplo5.criar_programa()
    tipo_valido, mensagem = Exemplo5.executar(programa)
    imprimir_execucao(programa, tipo_valido, mensagem)
