from sqlalchemy.orm import Mapped, relationship
from typing import List
from . import Config

class Departure(Config.BASE):
    name:Mapped[str]
    films:Mapped[List["Film"]] = relationship(back_populates="departure")
