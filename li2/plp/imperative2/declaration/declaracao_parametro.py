class DeclaracaoParametro:
    def __init__(self, identificador, tipo) -> None:
        self._id = identificador
        self._tipo = tipo

    def get_id(self):
        return self._id

    def get_tipo(self):
        return self._tipo

    def checa_tipo(self, ambiente) -> bool:
        return self._tipo.e_valido()

    def elabora(self, ambiente):
        ambiente.map(self._id, self._tipo)
        return ambiente
