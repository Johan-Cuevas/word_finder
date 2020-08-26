from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def new_route():
    form_words = request.form["word"]
    api_words = create_parameter1()
    return render_template("pass.html",  n = form_words, lots_words = api_words) 


def create_parameter1():
    dict_key = "ml"
    parameter = {dict_key: "ringing in the ear"}
    return create_request1(parameter)

def create_request1(request_data: dict):
    request = requests.get('https://api.datamuse.com/words', request_data)
    sound_json = request.json()
    return sound_json



if __name__ == "__main__":
    app.run(debug=True)

