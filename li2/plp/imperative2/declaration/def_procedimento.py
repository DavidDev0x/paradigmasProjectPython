from li2.plp.imperative2.util.tipo_procedimento import TipoProcedimento


class DefProcedimento:
    def __init__(self, parametros_formais, comando) -> None:
        self._parametros_formais = parametros_formais
        self._comando = comando

    def get_comando(self):
        return self._comando

    def get_parametros_formais(self):
        return self._parametros_formais

    def get_tipo(self):
        return TipoProcedimento(self._parametros_formais.get_tipos())
