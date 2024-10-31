from quart import Quart
from .db import Config


app = Quart(__name__)

from . import routes


def run():
    try:
        Config.up()
        app.run(port=8000)

    except Exception as e:
        raise e
    finally:
        Config.down()