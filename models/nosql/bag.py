from typing import List, Dict
from models.cursors import nosql_engine


class Bag:
    """
    TODO: Usar o ID do usuário como chave primária da bolsa.
    """
    def __init__(self) -> None:
        self._collection = nosql_engine.get_collection('bag')

    def set_item(self, user: str, items: List[Dict]) -> None:
        """
        Adiciona um item na bolsa do personagem.
        """
        return  # TODO: Terminar de desenvolver.

    def get_item(self, user: str, item: str) -> Dict:
        """
        Pega um item da bolsa.
        """
        return  # TODO: Terminar de desemvolver.
