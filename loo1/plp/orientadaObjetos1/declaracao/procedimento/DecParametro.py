class DecParametro:
    def __init__(self, identificador, tipo):
        self._id = identificador
        self._tipo = tipo

    def get_id(self):
        return self._id

    def get_tipo(self):
        return self._tipo

    def elabora(self, ambiente):
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._tipo.e_valido(ambiente)

    def declara_parametro(self, ambiente):
        ambiente.map(self._id, self._tipo)
        return ambiente
