from loo1.plp.expressions1.util.Tipo import Tipo
from loo1.plp.expressions1.util.ToStringProvider import ToStringProvider


class TipoProcedimento(Tipo):
    def __init__(self, tipos_parametros_formais: list[Tipo]):
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
            self._tipos_parametros_formais, "{", "}", ","
        )

    def intersecao(self, outro_tipo: Tipo):
        return self if outro_tipo.e_igual(self) else None
