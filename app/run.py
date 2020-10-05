from flask import Flask, render_template, request
from app.utils import datamuse_api
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def new_route():
    form_words = request.form["word"]
    api_words = datamuse_api.create_parameter(form_words)
    return render_template("pass.html",  form_response = form_words, lots_words = api_words) 



if __name__ == "__main__":
    app.run(debug=True)