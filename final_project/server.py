from machinetranslation import translator
from flask import Flask, render_template
import json

app = Flask("Web Translator")

@app.route("/englishToSpanish")
def englishToSpanish():
    ht = translator.english_to_spanish("Hello! How are you doing");
    return ht

@app.route("/spanishToEnglish")
def spanishToEnglish():
    ht = translator.spanish_to_english("Hola! Feliz Navidad!");
    return ht

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

