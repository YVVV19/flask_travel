from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from . import AutoTableNameMixin
class Base(DeclarativeBase, AutoTableNameMixin):
    ...


class Config(object):
    BASE = Base()
    ENGINE = create_engine("sqlite:///flask_travel.sql", echo=True)
    SESSION = sessionmaker(ENGINE)


    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)


    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(cls.ENGINE)