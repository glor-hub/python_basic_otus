"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask

from flask import (
    Blueprint,
    render_template,
)

app = Flask(__name__)

horoscope_app = Blueprint("horoscope_app", __name__)

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

@horoscope_app.get("/horoscope/")
def navbar():
    return render_template("base.html")

@horoscope_app.get("/", endpoint="hello")
def hello():
    return render_template("hello.html")

@horoscope_app.get("/about/", endpoint="about")
def about_signs():
    return render_template("about.html")

@horoscope_app.get("/zodiac_signs/", endpoint="signs_list")
def list_signs():
    return render_template("list.html", signs=list(ZODIAC_SIGNS.items()))

app.register_blueprint(horoscope_app, url_prefix="/")
