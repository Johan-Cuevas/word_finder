from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def new_route():
    form_words = request.form["word"]
    api_words = create_parameter(form_words)
    return render_template("pass.html",  form_response = form_words, lots_words = api_words) 


def create_parameter(user_resonse: str)-> str:
    dict_key = "ml"
    parameter = {dict_key: user_resonse}
    return create_request(parameter)

def create_request(dictionary_data: dict):
    request = requests.get('https://api.datamuse.com/words', dictionary_data)
    return process_request(request)

def process_request(request):
    json_data = request.json()
    return json_data



if __name__ == "__main__":
    app.run(debug=True)

