from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.valor_booleano import ValorBooleano
from li2.plp.imperative1.command.comando import Comando


class While(Comando):
    def __init__(self, expressao, comando) -> None:
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente):
        while True:
            condicao = exigir_tipo(self._expressao.avaliar(ambiente), ValorBooleano, "while")
            if not condicao.valor():
                return ambiente
            ambiente = self._comando.executar(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        return (
            self._expressao.checa_tipo(ambiente)
            and self._expressao.get_tipo(ambiente).e_booleano()
            and self._comando.checa_tipo(ambiente)
        )
