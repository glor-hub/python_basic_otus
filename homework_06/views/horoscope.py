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

from forms import HoroscopeForm
from models.database import db
from models import Horoscope

horoscopes_app = Blueprint("horoscopes_app", __name__)


@horoscopes_app.get("/")
def navbar():
    return render_template("base.html")


@horoscopes_app.get("/horoscopes/", endpoint="horoscopes_list")
def list_horoscopes():
    horoscopes: List[Horoscope] = Horoscope.query.all()
    return render_template("horoscopes/list.html", horoscopes=horoscopes)


@horoscopes_app.get("/<int:horoscope_id>/", endpoint="horoscope_details")
def get_horoscope(horoscope_id: int):
    horoscope = Horoscope.query.get(horoscope_id)
    if horoscope is None:
        raise NotFound(f"Horoscope #{horoscope_id} not found!")
    return render_template(
        "horoscopes/details.html",
        horoscope=horoscope,
    )


@horoscopes_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_horoscope():
    form = HoroscopeForm()
    if request.method == "GET":
        return render_template("horoscopes/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("horoscopes/add.html", form=form), HTTPStatus.BAD_REQUEST
    horoscope_name = form.data["name"]
    if not horoscope_name:
        raise BadRequest("Horoscope name is required, please fill `horoscope-name`")
    horoscope = Horoscope(name=horoscope_name)
    db.session.add(horoscope)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"could not save horoscope, probably name {horoscope_name!r} is not unique")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save horoscope, unexpected error")

    horoscope_url = url_for("horoscopes_app.horoscope_details", horoscope_id=horoscope.id)
    return redirect(horoscope_url)
