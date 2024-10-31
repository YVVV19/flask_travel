from sqlalchemy import select
from . import Departure, app, Config


@app.get("/departures")
def Departures():
    with Config.SESSION.begin() as session:
        smth=select(Departure)
        departures = session.scalars(smth).all()
        return departures