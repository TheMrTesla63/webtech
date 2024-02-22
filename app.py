from flask import Flask, render_template
app = Flask(__name__)

# Deze routes roepen allemaal iets aan en hierin kan je functies injecteren
@app.route("/informatie")   # 127.0.0.1:5000/informatie statische pagina
def info():
    return "<h1>Dit hebben we jou te bieden:</h1>"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/profiel/<naam>")  # zet de naam van de cursist in welkom.html
def cursist(naam):
    return render_template("welkom.html", naam=naam)

@app.route("/login")
def login():
    return render_template("inlog.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/films")
def films():
    return render_template("films.html")

@app.route("/regisseurs")
def regisseurs():
    return render_template("regisseurs.html")


if __name__ == "__main__":
    app.run(debug=True)
