from li2.plp.imperative1.command.comando import Comando


class ComandoDeclaracao(Comando):
    def __init__(self, declaracao, comando) -> None:
        self._declaracao = declaracao
        self._comando = comando

    def executar(self, ambiente):
        ambiente.incrementa()
        try:
            ambiente = self._declaracao.elabora(ambiente)
            return self._comando.executar(ambiente)
        finally:
            ambiente.restaura()

    def checa_tipo(self, ambiente) -> bool:
        ambiente.incrementa()
        try:
            return self._declaracao.checa_tipo(ambiente) and self._comando.checa_tipo(ambiente)
        finally:
            ambiente.restaura()
