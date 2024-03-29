from generate import ChatApp

chat = ChatApp()

def interactive():
    while True:
        com = input()
        if len(com) == 0 or com == "exit":
            break
        else:
            chat.chat(com)
    chat.save_to_file()

if __name__ == "__main__":
    interactive()
