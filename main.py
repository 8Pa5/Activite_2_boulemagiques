from flask import Flask, render_template
from random import choice

reponses_possible = [
" Essaye plus tard ",
" Essaye encore ",
" Pas d'avis ",
" C'est ton destin ",
" Le sort en est jeté ",
" Une chance sur deux ",
" Repose ta question ",
" D'après moi oui ",
 "C'est certain ",
" Oui absolument ",
" Tu peux compter dessus ",
" Sans aucun doute ",
" Très probable ",
" Oui ",
" C'est bien parti ",
" C'est non ",
" Peu probable ",
" Faut pas rêver " ,
" N'y compte pas ",
" Impossible ",
]

app = Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def index():
    reponse=0

    if request.method == "POST":



    return render_template("index.html")




app.run(host = '0.0.0.0', port = 81)