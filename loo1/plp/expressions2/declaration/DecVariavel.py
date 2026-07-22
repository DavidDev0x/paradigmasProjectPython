class DecVariavel:
    def __init__(self, identificador, expressao):
        self._id = identificador
        self._expressao = expressao

    def get_id(self):
        return self._id

    def get_expressao(self):
        return self._expressao
