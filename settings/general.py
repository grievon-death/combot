import os


# SQL Database configuration.
SQL_CONF = {
    'host': os.environ.get('SQL_HOST', '127.0.0.1'),
    'port': int(os.environ.get('SQL_PORT', '5432')),
    'user': os.environ.get('SQL_USER', 'root'),
    'password': os.environ.get('SQL_PASSWORD', 'root'),
    'db': os.environ.get('SQL_DB', 'combot'),
}

# NOSQL Database configuration.
NOSQL_CONF = {
    'host': os.environ.get('NOSQL_HOST', '127.0.0.1'),
    'port': int(os.environ.get('NOSQL_PORT', '27017')),
    'user': os.environ.get('NOSQL_USER', 'root'),
    'password': os.environ.get('NOSQL_PASSWORD', 'root'),
    'db': os.environ.get('NOSQL_DB', 'combot'),
}

# Discord BOT Token
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Configuração de logs
LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()
LOGCONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(levelname)s][%(name)s:%(lineno)s] -> %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': LOGLEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
        'combot': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
