# TODO: Criar cursores para o bancos SQL, NOSQL e SQlite3.

# SQL: Pode ser Mysql. Será usado para os dados gerais dos personagens(jogadores);

# NOSQL: Será usado para iniciar as ações de personagem. Eg: Batalhas, Lojas, Expedições.

from sqlalchemy.ext.asyncio import create_async_engine
from pymongo import MongoClient

from settings.general import SQL_CONF, NOSQL_CONF


SQL_URL =  'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
    SQL_CONF['user'],
    SQL_CONF['password'],
    SQL_CONF['host'],
    SQL_CONF['port'],
    SQL_CONF['db'],
)

sql_engine = create_async_engine(
    SQL_URL,
    echo=True, # Loga informações de conexão com o banco de dados.
)

nosql_engine = MongoClient(
    'mongodb://{}:{}@{}:{}'.format(
        NOSQL_CONF['user'],
        NOSQL_CONF['password'],
        NOSQL_CONF['host'],
        NOSQL_CONF['port'],
    )
)[NOSQL_CONF['db']]
