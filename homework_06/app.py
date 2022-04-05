from os import getenv

from flask import Flask

from flask import (
    render_template,
)

from flask_migrate import Migrate

from models.database import db
from models import Zodiac

from views.zodiac import zodiacs_app
from views.horoscope import horoscopes_app

app = Flask(__name__)

CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJECT_PATH)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(horoscopes_app, url_prefix="/horoscope")
app.register_blueprint(zodiacs_app, url_prefix="/zodiac_signs")

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
    for (key,value) in list(ZODIAC_SIGNS.items()):
        zodiac = Zodiac(name=value)
        db.session.add(zodiac)
        db.session.commit()

@app.get("/", endpoint="hello")
def hello():
    return render_template("hello.html")

@app.get("/about/", endpoint="about")
def about_signs():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
