import json
import logging
from typing import Dict, List

_log = logging.getLogger(__name__)


async def get_populate_content() -> Dict:
    """
    Lê  conteúdo do arquivo populate.json
    """
    try:
        _log.info('Lendo arquivo.')
        _content: str

        with open('populate.json') as _file:
            _content = _file.read()

        return json.loads(_content)
    except FileNotFoundError as e:
        _log.error('Arquivo com informações para serem populadas não foi encontrado.')
        raise Exception(e.args)
    except Exception as e:
        _log.debug('Problema não esperado!')
        raise Exception(e.args)


async def validate_max_points_distribituion(max_points: int, classes: List[Dict]) -> bool:
    """
    Valida a quantidade de pontos distribuídos nas classes.
    """
    for job in classes:
        _name = job.pop('name')
        _values = list(job.values())

        try:
            if sum(_values) != max_points:
                return False
        except TypeError as e:
            _log.error('Tipo inesperado nas pontuações.')
            return False
    
    del _name
    del _values

    return True
