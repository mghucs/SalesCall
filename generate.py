from openai import OpenAI
import os
import json
import re
import time

class ChatApp:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.messages = [
            {"role": "system", "content": "We are in a sales call, and your name is Staya and my name is Sam."}
        ]

    def chat(self, message):
        """ Puts a new line of dialogue to the chat transcript
        and receive a reply
        :param message: Message to be posted to the conversation
        """
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        print(reply)
        return reply

    def save(self):
        """Saves the chat history to a JSON file."""
        try:
            ts = time.time()
            json_object = json.dumps(self.messages, indent=4)
            with open(f"{ts}.json", "w") as outfile:
                outfile.write(json_object)
        except:
            os._exit(1)

    def load(self, load_file):
        """Loads chat history from a file.
        :param load_file: Path to the file containing the chat history.
        """
        with open(load_file) as f:
            self.messages = json.load(f)
    
    def ask(self, load_file, question):
        """Takes a call transcript and a user question as command line 
        arguments and answers the user’s question in relation to the call 
        transcript.
        :param load_file: Path to the file containing the chat history.
        :param question: Question in relation to the call history.
        """
        self.load(load_file)
        self.chat(question)

chat = ChatApp()

# 3
# chat.ask("We-are-in-a-sales-call-and-yo-1711582745-811244.json", "What product was the customer interested in?")