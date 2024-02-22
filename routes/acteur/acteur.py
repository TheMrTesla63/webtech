from flask import Blueprint, render_template, session, request, redirect, url_for

from extensions import db
from models.acteur import Acteur

# from ...models.auction import Auction
# from ..auth.auth import login_required, get_user

acteur = Blueprint("acteur", __name__, static_folder="static", template_folder="templates")

@acteur.route("/", methods = ["GET"])
def getPageacteur():

  acteurs = Acteur.query.all()
  return render_template("acteur.html", length=len(acteurs), acteurs=acteurs)


