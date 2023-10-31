
from tornado.web import Application

from core.api.views import classes


def app():
    return Application([
        (r"/possible-classes", classes.PossibleClassesView),
    ])
