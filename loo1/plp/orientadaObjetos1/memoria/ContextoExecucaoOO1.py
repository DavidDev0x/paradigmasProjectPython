from .AmbienteExecucaoOO1 import AmbienteExecucaoOO1
from loo1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoJaDeclaradoException import ObjetoJaDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoNaoDeclaradoException import ObjetoNaoDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.execucao.EntradaInvalidaException import EntradaInvalidaException
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.orientadaObjetos1.expressao.valor.ValorString import ValorString
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ContextoExecucaoOO1(AmbienteExecucaoOO1):
    def __init__(self, entrada_ou_ambiente=None):
        self._pilha: list[dict] = []
        self._map_objetos: dict = {}
        self._map_def_classe: dict = {}
        self._entrada = None
        self._saida = ListaValor()
        self._prox_ref: ValorRef | None = None

        if isinstance(entrada_ou_ambiente, AmbienteExecucaoOO1):
            ambiente = entrada_ou_ambiente
            self._prox_ref = ambiente.get_ref()
            self._map_objetos = ambiente.get_map_objetos()
            self._map_def_classe = ambiente.get_map_def_classe()
            self._entrada = ambiente.get_entrada()
            self._saida = ambiente.get_saida()
            self._pilha = [{Id("this"): ValorNull()}]
        else:
            self._entrada = entrada_ou_ambiente

    def get_pilha(self) -> list[dict]:
        return self._pilha

    def set_pilha(self, pilha: list[dict]) -> None:
        self._pilha = pilha

    def set_saida(self, saida) -> None:
        self._saida = saida

    def get_map_def_classe(self) -> dict:
        return self._map_def_classe

    def get_map_objetos(self) -> dict:
        return self._map_objetos

    def get_saida(self):
        return self._saida

    def get_entrada(self):
        return self._entrada

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError("Não há escopo de execução para restaurar.")
        self._pilha.pop()

    def map(self, identificador, valor) -> None:
        if not self._pilha:
            raise RuntimeError("Crie um escopo antes de mapear valores.")
        if identificador in self._pilha[-1]:
            raise VariavelJaDeclaradaException(identificador)
        self._pilha[-1][identificador] = valor

    def get(self, identificador):
        for escopo in reversed(self._pilha):
            if identificador in escopo and escopo[identificador] is not None:
                return escopo[identificador]
        raise VariavelNaoDeclaradaException(identificador)

    def get_valor(self, identificador):
        return self.get(identificador)

    def change_valor(self, identificador, valor) -> None:
        for escopo in reversed(self._pilha):
            if identificador in escopo:
                escopo[identificador] = valor
                return
        raise VariavelNaoDeclaradaException(identificador)

    def map_def_classe(self, identificador, definicao) -> None:
        if identificador in self._map_def_classe:
            raise ClasseJaDeclaradaException(identificador)
        self._map_def_classe[identificador] = definicao

    def get_def_classe(self, identificador):
        if identificador not in self._map_def_classe:
            raise ClasseNaoDeclaradaException(identificador)
        return self._map_def_classe[identificador]

    def map_objeto(self, referencia, objeto) -> None:
        if referencia in self._map_objetos:
            raise ObjetoJaDeclaradoException(objeto.get_classe())
        self._map_objetos[referencia] = objeto

    def get_objeto(self, referencia):
        if referencia not in self._map_objetos:
            raise ObjetoNaoDeclaradoException(referencia)
        return self._map_objetos[referencia]

    def get_ref(self) -> ValorRef:
        if self._prox_ref is None:
            self._prox_ref = ValorRef(ValorRef.VALOR_INICIAL)
        return self._prox_ref

    def get_prox_ref(self) -> ValorRef:
        atual = ValorRef(self.get_ref().valor())
        self._prox_ref.incrementa()
        return atual

    def write(self, valor):
        self._saida.write(valor)
        return self

    def _le_entrada(self) -> str:
        if self._entrada is None:
            return input()
        if self._entrada.length() == 0:
            raise EntradaInvalidaException("Número de argumentos menor do que o número de reads.")
        valor = str(self._entrada.get_head())
        self._entrada = self._entrada.get_tail()
        return valor

    def read(self, tipo):
        texto = self._le_entrada().strip()
        if not isinstance(tipo, TipoPrimitivo):
            raise EntradaInvalidaException("A variável lida deve possuir tipo primitivo.")
        try:
            if tipo.e_booleano():
                if texto.lower() not in {"true", "false"}:
                    raise ValueError
                return ValorBooleano(texto.lower() == "true")
            if tipo.e_inteiro():
                return ValorInteiro(int(texto))
            if tipo.e_string():
                return ValorString(texto)
        except ValueError as exc:
            raise EntradaInvalidaException(
                "O tipo da entrada e o da variável a ser lida são diferentes."
            ) from exc
        raise EntradaInvalidaException("Tipo de entrada inválido.")

    def get_contexto_id_valor(self):
        ambiente = ContextoExecucaoOO1(self._entrada)
        ambiente._pilha = self._pilha
        ambiente._saida = self._saida
        return ambiente

    def __str__(self) -> str:
        linhas: list[str] = []
        for escopo in reversed(self._pilha):
            linhas.extend(f"{identificador} {valor}" for identificador, valor in escopo.items())
        linhas.extend(f"{ref} {objeto}" for ref, objeto in self._map_objetos.items())
        return "\n".join(linhas)
