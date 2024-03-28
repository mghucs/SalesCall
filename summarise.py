import ChatApp
# Add command 
chat = ChatApp()

def summarise():
    chat.load("1711586593.7863522.json")
    chat.chat("Can you generate me a summary of the key points from our call?")

if __name__ == "__main__":
    summarise()