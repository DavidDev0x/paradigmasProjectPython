from __future__ import annotations

from dataclasses import dataclass

from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import (
    ExpAnd,
    ExpConcat,
    ExpDeclaracao,
    ExpEquals,
    ExpLength,
    ExpMenos,
    ExpNot,
    ExpOr,
    ExpSoma,
    ExpSub,
    Expressao,
    Id,
    ValorBooleano,
    ValorInteiro,
    ValorString,
)
from le2.plp.expressions2.memory.tipo_invalido_exception import TipoInvalidoException
from le2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from le2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from le2.plp.expressions2.programa import Programa


@dataclass(frozen=True)
class ResultadoExemplo:
    nome: str
    tipo_valido: bool | str
    resultado: str
    esperado: str
    ok: bool


class Exemplos:
    @staticmethod
    def _executar_expressao(nome: str, exp: Expressao, esperado: str, deve_ser_tipo_valido: bool = True) -> ResultadoExemplo:
        programa = Programa(exp)
        try:
            tipo_valido = programa.checa_tipo()
        except (VariavelJaDeclaradaException, VariavelNaoDeclaradaException) as exc:
            tipo_valido = f"erro: {exc}"

        try:
            resultado = str(programa.executar())
        except (TipoInvalidoException, VariavelJaDeclaradaException, VariavelNaoDeclaradaException) as exc:
            resultado = f"erro: {type(exc).__name__}: {exc}"

        if deve_ser_tipo_valido:
            ok = (tipo_valido is True) and (resultado == esperado)
        else:
            tipo_indica_erro = (tipo_valido is False) or (isinstance(tipo_valido, str) and tipo_valido.startswith("erro:"))
            ok = tipo_indica_erro and resultado.startswith(esperado)
        return ResultadoExemplo(nome, tipo_valido, resultado, esperado, ok)

    @staticmethod
    def criar_exemplos() -> list[tuple[str, Expressao, str, bool]]:
        return [
            ("soma inteira: 1 + 2", ExpSoma(ValorInteiro(1), ValorInteiro(2)), "3", True),
            ("subtração inteira: 7 - 4", ExpSub(ValorInteiro(7), ValorInteiro(4)), "3", True),
            ("menos unário: -5", ExpMenos(ValorInteiro(5)), "-5", True),
            ("and lógico: true and false", ExpAnd(ValorBooleano(True), ValorBooleano(False)), "false", True),
            ("or lógico: false or true", ExpOr(ValorBooleano(False), ValorBooleano(True)), "true", True),
            ("not lógico: ~false", ExpNot(ValorBooleano(False)), "true", True),
            ("concatenação: 'LE' ++ '2'", ExpConcat(ValorString("LE"), ValorString("2")), "LE2", True),
            ("length string: length('abc')", ExpLength(ValorString("abc")), "3", True),
            ("igualdade inteira: 3 == 3", ExpEquals(ValorInteiro(3), ValorInteiro(3)), "true", True),
            (
                "let simples: let var x = 1 in x + 1",
                ExpDeclaracao([DecVariavel(Id("x"), ValorInteiro(1))], ExpSoma(Id("x"), ValorInteiro(1))),
                "2",
                True,
            ),
            (
                "erro de tipo: true + 2",
                ExpSoma(ValorBooleano(True), ValorInteiro(2)),
                "erro: TipoInvalidoException",
                False,
            ),
            (
                "erro de tipo: length(10)",
                ExpLength(ValorInteiro(10)),
                "erro: TipoInvalidoException",
                False,
            ),
            (
                "erro de tipo: 'a' and true",
                ExpAnd(ValorString("a"), ValorBooleano(True)),
                "erro: TipoInvalidoException",
                False,
            ),
            (
                "erro de declaração duplicada no mesmo bloco",
                ExpDeclaracao(
                    [DecVariavel(Id("x"), ValorInteiro(1)), DecVariavel(Id("x"), ValorInteiro(2))],
                    Id("x"),
                ),
                "erro: VariavelJaDeclaradaException",
                False,
            ),
        ]

    @staticmethod
    def executar_todos() -> list[ResultadoExemplo]:
        resultados: list[ResultadoExemplo] = []
        for nome, exp, esperado, tipo_valido in Exemplos.criar_exemplos():
            resultados.append(Exemplos._executar_expressao(nome, exp, esperado, tipo_valido))
        return resultados


if __name__ == "__main__":
    for resultado in Exemplos.executar_todos():
        status = "OK" if resultado.ok else "FALHOU"
        print(f"[{status}] {resultado.nome}")
        print(f"  Tipo válido: {resultado.tipo_valido}")
        print(f"  Resultado: {resultado.resultado}")
        print(f"  Esperado: {resultado.esperado}")
