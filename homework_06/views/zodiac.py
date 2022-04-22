from http import HTTPStatus
from sqlite3 import IntegrityError, DatabaseError

from typing import List

from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
)

from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from models.database import db
from models import Zodiac

zodiacs_app = Blueprint("zodiacs_app", __name__)

zodiac_db_update_flag: bool = False

ZODIAC_SIGNS = {
    1: "Aries",
    2: "Leo",
    3: "Sagittarius",
    4: "Taurus",
    5: "Virgo",
    6: "Capricorn",
    7: "Gemini",
    8: "Libra",
    9: "Aquarius",
    10: "Cancer",
    11: "Scorpio",
    12: "Pisces",
}
def update_db():
    for (key, value) in list(ZODIAC_SIGNS.items()):
        zodiac = Zodiac(name=value)
        db.session.add(zodiac)
        db.session.commit()

@zodiacs_app.get("/", endpoint="zodiacs_list")
def list_zodiacs():
    zodiacs: List[Zodiac] = Zodiac.query.all()
    if zodiacs==[] or zodiacs == None:
        update_db()
        zodiacs: List[Zodiac] = Zodiac.query.all()
    return render_template("zodiacs/list.html", zodiacs=list(zodiacs))
