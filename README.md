# Project description
A project to generate a sales call and allow the user to interact with an assistant
as though the user were buying something or any other queries related to sales

# Setup Instructions
```pip install -r requirements.txt```

# Usage Guide
```python interactive.py``` for chatting

```python summarise.py [file-name]``` to summarise a call transcript

```python ask.py [file-name] [question]``` to ask a question based on an inputted call transcript

# Testing
```python -m unittest discover -v``` to run all tests
```python -m unittest test.Test.[test_name] -v``` to run specific test

# Thought Process
I used a [github repo](https://github.com/stancsz/chatgpt/blob/master/ChatGPT.py) for reference.

I started with OpenAI's quickstart and looked at examples to learn how to generate chat completions. Then I organised the code based on objects. A central generate.py app with all the functions for chatting, saving, and loading. I created scripts based on each of the question prompts.

I tested functionality with French and Spanish and lastly added Unittests