from flask import Blueprint, render_template, session, request, redirect, url_for

from extensions import db
from models.film import Film
from models.regisseur import Regisseur



film = Blueprint("film", __name__, static_folder="static", template_folder="templates")


@film.route("/", methods = ["GET"])
def getPageFilms():
    films = []
    regs = []
    for film, reg in db.session.query(Film, Regisseur).filter(Film.id_regisseur == Regisseur.id).all():
        films.append(film)
        regs.append(reg)
    
    return render_template("films.html", length=len(films), films=films, regs=regs)

@film.route("/<id>", methods = ["GET"])
def getPageFilm(id):
    film = Film.query.filter_by(id=id).first()
    
    if film is None:
        print("error")

    reg = Regisseur.query.filter_by(id=film.id_regisseur).first()
    return render_template("film.html", film=film, reg=reg)
