from li2.plp.expressions1.util.tipo import Tipo
from li2.plp.expressions1.util.to_string_provider import ToStringProvider


class TipoProcedimento(Tipo):
    def __init__(self, tipos_parametros_formais: list) -> None:
        self._tipos_parametros_formais = list(tipos_parametros_formais)

    def e_booleano(self) -> bool:
        return False

    def e_inteiro(self) -> bool:
        return False

    def e_string(self) -> bool:
        return False

    def e_igual(self, tipo: Tipo) -> bool:
        if isinstance(tipo, TipoProcedimento):
            return self._tipos_parametros_formais == tipo._tipos_parametros_formais
        return tipo.e_igual(self)

    def e_valido(self) -> bool:
        return all(tipo.e_valido() for tipo in self._tipos_parametros_formais)

    def get_nome(self) -> str:
        return ToStringProvider.list_to_string(
            self._tipos_parametros_formais, ",", "{", "}"
        )

    def intersecao(self, outro_tipo: Tipo):
        return self if outro_tipo.e_igual(self) else None

    def __str__(self) -> str:
        return self.get_nome()

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, TipoProcedimento) and self.e_igual(outro)

    def __hash__(self) -> int:
        return hash(tuple(self._tipos_parametros_formais))
