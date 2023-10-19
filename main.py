"""
Arquivo com chamada das principais funções do sistema no formado de comando.
"""
import logging
from argparse import ArgumentParser

_loger = logging.getLogger(__name__)

parser = ArgumentParser(description='Combot command handler.')
parser.add_argument(
    'command',
    action='store',
    type=str,
    help='[run, migrate, test]'
)
args = parser.parse_args()


if __name__ == '__main__':

    match args.command:
        case 'test':
            _loger.info('Ok,seems all right')
        case _:
            parser.print_help()
