import requests

def create_parameter(user_resonse: str)-> str:
    dict_key = "ml"
    parameter = {dict_key: user_resonse}
    return create_request(parameter)

def create_request(dictionary_data: dict):
    request = requests.get('https://api.datamuse.com/words', dictionary_data)
    return process_request(request)

def process_request(request):
    json_data = request.json()
    return shorten_word_list(json_data)

def shorten_word_list(data):
    word_list = data[0:3] # only grabs first three words
    return word_list