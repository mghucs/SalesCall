from openai import OpenAI
from mongo import Mongo
import os
import json
import re
import time

class ChatApp:
    def __init__(self):
        self.mongo = Mongo()
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

    def save_to_file(self):
        """Saves the chat history to a JSON file."""
        try:
            ts = time.time()
            json_object = json.dumps(self.messages, indent=4)
            with open(f"{ts}.json", "w") as outfile:
                outfile.write(json_object)
        except:
            os._exit(1)

    def save_to_db(self):
        """Saves the chat history to MongoDB."""
        ts = time.time()
        to_insert = {f"{int(ts)}": self.messages}
        self.mongo.insert(to_insert)

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
