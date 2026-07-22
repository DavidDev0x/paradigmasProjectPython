from .Comando import Comando
from .Atribuicao import Atribuicao
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoObjeto import ContextoObjeto
from loo1.plp.orientadaObjetos1.memoria.Objeto import Objeto
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class New(Comando):
    def __init__(self, av, classe):
        self._av = av
        self._classe = classe

    def executar(self, ambiente):
        definicao = ambiente.get_def_classe(self._classe)
        auxiliar = ContextoExecucaoOO1(ambiente)
        definicao.get_dec_variavel().elabora(auxiliar)
        estado = ContextoObjeto(auxiliar.get_pilha().pop())
        objeto = Objeto(self._classe, estado)
        referencia = ambiente.get_prox_ref()
        ambiente.map_objeto(referencia, objeto)
        Atribuicao(self._av, referencia).executar(ambiente)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        tipo_classe = TipoClasse(self._classe)
        return self._av.checa_tipo(ambiente) and tipo_classe.e_valido(ambiente) and tipo_classe == self._av.get_tipo(ambiente)

    def get_classe(self):
        return self._classe

    def get_av(self):
        return self._av
