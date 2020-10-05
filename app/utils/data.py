import requests
#this is testing for the api to learn how it works
# api returns a json filled with response so now I would need to return the word

def user_prompt():
    print("Option 1 enter the word you are describing")
    print("Option 2")
    user_input()

def user_input()-> int:
    user_response = int(input("Enter 1 for option 1, enter 2 for option 2: "))
    return check_user_response(user_response)

def check_user_response(response: int):
    if response == 1:
        return create_parameter("ml")

def create_parameter(response: str):
    dict_key = response
    word = input("Enter word you are describing: ")
    parameter = {dict_key: word}
    return create_request(parameter)

def create_request(request_data: dict):
    request = requests.get('https://api.datamuse.com/words', request_data)
    sound_json = request.json()
    print(sound_json[0], "This is the first entery in the dictionary")
    list_of_words = sound_json[0:3]
    print(list_of_words)
    for i in list_of_words:
        print(i["word"], "This should print out 3 words on single lines")

def create_parameter1():
    dict_key = "ml"
    parameter = {dict_key: "ringing in the ear"}
    return create_request1(parameter)

def create_request1(request_data: dict):
    request = requests.get('https://api.datamuse.com/words', request_data)
    sound_json = request.json()
    print(sound_json)
    return sound_json

if  __name__ == "__main__":
    user_prompt()