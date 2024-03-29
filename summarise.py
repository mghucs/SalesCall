from generate import ChatApp
from sys import argv
file = "1711586593.7863522.json" if len(argv) == 1 else argv[1]
chat = ChatApp()

def summarise():
    chat.load(file)
    chat.chat("Can you generate me a summary of the key points from our call?")
    chat.save_to_db()

if __name__ == "__main__":
    summarise()