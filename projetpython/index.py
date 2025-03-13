from flask import Flask, render_template, request, redirect, url_for

import datetime

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulaire")
def formulaire():
  return render_template("formulaire.html")

@app.route("/traitement1", methods=["POST", "GET"])
def traitement1():
  if request.method=="POST":
   données=request.form #pour recupérer les donnés d'un formulaire
   nom= données.get('nom')
   prenom=données.get('prenom')
   date=données.get('date')
   Email=données.get('Email')
   sexe=données.get('sexe')
   Etude=données.get('Etude')
   language= données.get('language')
   sicence= données.get('sicence')
   découvert= données.get('découvert')
   filiére=données.get('filiére')
   print(nom,prenom,language,sicence,découvert,filiére,Email,sexe,date,Etude)
   return render_template("traitement1.html",nom_utilisateur=prenom)
  else:
    return redirect(url_for('index'))

if __name__=='__main__':
  app.run(debug=True)