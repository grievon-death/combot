#!/usr/bin/env python3.10
"""
Arquivo com chamada das principais funções do sistema no formado de comando.
"""
from logging import config as logger
from argparse import ArgumentParser

from core.utils.system_commands import Command
from settings.general import LOGCONF

parser = ArgumentParser(description='Combot command handler.')
parser.add_argument(
    'command',
    action='store',
    type=str,
    help='[run, migrate, test]'
)
args = parser.parse_args()


if __name__ == '__main__':
    logger.dictConfig(LOGCONF)

    match args.command:
        case 'migrate':
            Command.migrate()
        case _:
            parser.print_help()
