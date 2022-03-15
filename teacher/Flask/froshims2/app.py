from flask import Flask, render_template, request

app = Flask(__name__)

INSCRITS = {}

SPORTS = [
    "Basketball",
    "Football",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Valider l'inscription
    if not request.form.get("name"):
        return render_template("failure.html", message="Nom manquant")

    #Valider le sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("failure.html", message="Sport invalide")
    if sport not in SPORTS:
        return render_template("failure.html", message="Pas de sport sélectionné")

    #Retenir l'inscrit
    INSCRITS[name] = sport

    #Confirmer l'inscription
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=INSCRITS)

