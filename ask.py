from generate import ChatApp
from sys import argv

file = "1711586593.7863522.json" if len(argv) == 1 else argv[1]
question = "What product was the customer interested in?" if len(argv) == 2 else argv[2]

chat = ChatApp()

def ask():
    chat.ask(file, question)

if __name__ == "__main__":
    ask()

