from flask import Blueprint, render_template, session, request, redirect, url_for

from extensions import db
from models.regisseur import Regisseur

# from ...models.auction import Auction
# from ..auth.auth import login_required, get_user

regisseur = Blueprint("regisseur", __name__, static_folder="static", template_folder="templates")

@regisseur.route("/", methods = ["GET"])
def getRegisseurs():
  regisseurs = Regisseur.query.all()
  return render_template("regisseurs.html", length=len(regisseurs), regisseurs=regisseurs)

@regisseur.route("/<id>", methods = ["GET"])
def getRegisseur(id):
  regisseur = Regisseur.query.filter_by(id=id).first()
  return render_template("regisseur.html", regisseurs=regisseur)


