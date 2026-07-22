from li2.plp.imperative1.declaration.declaracao import Declaracao


class DeclaracaoProcedimento(Declaracao):
    def __init__(self, identificador, def_procedimento) -> None:
        self._id = identificador
        self._def_procedimento = def_procedimento

    def elabora(self, ambiente):
        ambiente.map_procedimento(self._id, self._def_procedimento)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        ambiente.map(self._id, self._def_procedimento.get_tipo())
        parametros = self._def_procedimento.get_parametros_formais()
        if not parametros.checa_tipo(ambiente):
            return False
        ambiente.incrementa()
        try:
            parametros.elabora(ambiente)
            return self._def_procedimento.get_comando().checa_tipo(ambiente)
        finally:
            ambiente.restaura()
