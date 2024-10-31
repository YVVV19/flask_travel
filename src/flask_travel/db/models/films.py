from .departure import Departure
from decimal import Decimal
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from . import Config

class Film(Config.BASE):
    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]
    desc:Mapped[str]
    departure:Mapped[Departure] = relationship(back_populates="films")
    departure_id:Mapped[int] = mapped_column(ForeignKey("departures.id"))
    price:Mapped[Decimal]
