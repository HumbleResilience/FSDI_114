from random import choice
import requests
from datetime import datetime

URL = "http://127.0.0.1:5000/messages"
GREETINGS = [
    "hello",
    "howdy",
    "how are you?",
    "greetings",
    "boas",
    "hola",
    "hey"
]


def post_greeting():
    greeting = {"message": ""}
    greeting["timestamp"] = datetime.now().strftime("%F %H:%M:%S")
    greeting["message"] = choice(GREETINGS)
    response = requests.post(URL, json=greeting)
    if response.status_code == 204:
        print("Message Posted")
    else:
        print("ERROR Received")

if __name__ == "__main__":
    for _ in range(100):
        post_greeting()

