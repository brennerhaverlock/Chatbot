# -*- coding: utf-8 -*-

from random import choice

# combine functions and conditionals to get a response from the bot


def get_topic(topic_response):

    # add some bot responses to this list

    humor = ["Two things are infinite: the universe and human stupidity and I'm not sure about the universe. ― Albert Einstein ",
             "You only live once, but if you do it right, once is enough.       ― Mae West",
             "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid. ― Jane Austen, Northanger Abbey"]
    religion = []
    wisdom = [2]
    death = [3]
    romance = [4]

    if topic_response == "humor":
        return choice(humor)
    elif topic_response == "religion":
        return choice(religion)
    elif topic_response == "wisdon":
        return choice(wisdom)
    else:
        return "Please enter a quote section or 'done' to leave"


print("Welcome to Quote Bot")
print("Please enter a category")

topic_response = ""
# TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:

    topic_response = str(input("What topic are you interested in? "))

    # Quits program when user responds with 'done'
    if topic_response == 'done':
        break

    bot_response = get_topic(topic_response)
    print(bot_response)
