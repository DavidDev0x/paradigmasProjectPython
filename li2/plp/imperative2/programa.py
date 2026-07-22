class Programa:
    def __init__(self, comando) -> None:
        self._comando = comando

    def executar(self, ambiente):
        ambiente = self._comando.executar(ambiente)
        return ambiente.get_saida()

    def checa_tipo(self, ambiente) -> bool:
        return self._comando.checa_tipo(ambiente)
