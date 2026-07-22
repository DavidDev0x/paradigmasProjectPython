from li2.plp.imperative1.command.comando import Comando
from li2.plp.imperative2.util.tipo_procedimento import TipoProcedimento


class ChamadaProcedimento(Comando):
    def __init__(self, nome_procedimento, parametros_reais) -> None:
        self._nome_procedimento = nome_procedimento
        self._parametros_reais = parametros_reais

    def executar(self, ambiente):
        procedimento = ambiente.get_procedimento(self._nome_procedimento)
        valores = self._parametros_reais.avaliar(ambiente).to_list()
        formais = list(procedimento.get_parametros_formais())
        if len(valores) != len(formais):
            raise ValueError(
                f"Procedimento {self._nome_procedimento}: esperado(s) {len(formais)} parâmetro(s), recebido(s) {len(valores)}."
            )
        ambiente.incrementa()
        try:
            for formal, valor in zip(formais, valores):
                ambiente.map(formal.get_id(), valor)
            return procedimento.get_comando().executar(ambiente)
        finally:
            ambiente.restaura()

    def checa_tipo(self, ambiente) -> bool:
        tipo_procedimento = ambiente.get(self._nome_procedimento)
        tipo_reais = TipoProcedimento(self._parametros_reais.get_tipos(ambiente))
        return tipo_procedimento.e_igual(tipo_reais)
