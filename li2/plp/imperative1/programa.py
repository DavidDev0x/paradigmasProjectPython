class Programa:
    def __init__(self, comando) -> None:
        self._comando = comando

    def executar(self, ambiente_execucao):
        ambiente_execucao = self._comando.executar(ambiente_execucao)
        return ambiente_execucao.get_saida()

    def checa_tipo(self, ambiente_compilacao) -> bool:
        return self._comando.checa_tipo(ambiente_compilacao)
