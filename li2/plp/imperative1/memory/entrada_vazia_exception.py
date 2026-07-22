class EntradaVaziaException(Exception):
    def __init__(self) -> None:
        super().__init__("Entrada vazia.")
