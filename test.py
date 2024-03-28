from unittest import TestCase

from generate import ChatApp

class Test(TestCase):
    def test_interactive(self):
        print("<< (enter your prompts)")
        chat = ChatApp()
        # chat.save()
        while True:
            message = input()
            if len(message) == 0 or message == "exit":
                break
            else:
                chat.chat(message)
    def test_load(self):
        chat = ChatApp()
        chat.load("1711586593.7863522.json")
        chat.chat("Can you generate me a summary of the key points from our call?")
    def test_save(self):
        chat = ChatApp()
        print("<< (enter your prompts to be saved)")
        chat = ChatApp() if chat == None else chat
        # chat.save()
        while True:
            message = input()
            if len(message) == 0 or message == "exit":
                break
            else:
                chat.chat(message)
        chat.save()
    def test_ask(self):
        chat = ChatApp()
        chat.ask("1711586593.7863522.json", "What product was the customer interested in?")