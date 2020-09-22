# -*- coding: utf-8 -*-

from random import choice

# combine functions and conditionals to get a response from the bot


def get_topic(topic_response):

    # add some bot responses to this list

    humor = ["Two things are infinite: the universe and human stupidity and I'm not sure about the universe. ― Albert Einstein ",
             "You only live once, but if you do it right, once is enough.       ― Mae West",
             "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid. ― Jane Austen, Northanger Abbey",
             "“A day without sunshine is like, you know, night.”― Steve Martin ",
             "“Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.” ― Garrison Keillor ",
             "“Some people never go crazy. What truly horrible lives they must lead.”― Charles Bukowski ",
             "Reality continues to ruin my life.”― Bill Watterson",
             "“I am free of all prejudice. I hate everyone equally. ”― W.C. Fields "]
    religion = [
        "“Science without religion is lame, religion without science is blind.”― Albert Einstein ",
        "“The mind is its own place, and in itself can make a heaven of hell, a hell of heaven..”― John Milton, Paradise Lost ",
        "“In heaven, all the interesting people are missing.”― Friedrich Nietzsche",
        "“Hate the sin, love the sinner.”― Mahatma Gandhi ",
        "“Science and religion are not at odds. Science is simply too young to understand.”― Dan Brown, Angels & Demons ",
        "“Forgive, O Lord, my little jokes on Thee And I'll forgive Thy great big one on me.” - Robert Frost",
        "“My concern is not whether God is on our side; my greatest concern is to be on God's side, for God is always right. ― Abraham Lincoln "

    ]
    wisdom = ["“Knowing yourself is the beginning of all wisdom.” ― Aristotle "
              "“The only true wisdom is in knowing you know nothing.”― Socrates",
              "“Count your age by friends, not years. Count your life by smiles, not tears.”― John Lennon ",
              "“In a good bookroom you feel in some mysterious way that you are absorbing the wisdom contained in all the books through your skin, without even opening them.” ― Mark Twain ",
              "“May you live every day of your life.”― Jonathan Swift  ",
              "“Never laugh at live dragons.” -J.R.R. Tolkien "]

    death = ["“To the well-organized mind, death is but the next great adventure.” - J.K Rowling",
             "“I'm not afraid of death; I just don't want to be there when it happens.” - Woody Allen ",
             "“Death ends a life, not a relationship.” - Mitch Albom, Tuesdays with Morrie ",
             " “A thing is not necessarily true because a man dies for it.” ― Oscar Wilde ",
             "“I do not fear death. I had been dead for billions and billions of years before I was born, and had not suffered the slightest inconvenience from it.” ― Mark Twain ",
             " “It kills me sometimes, how people die.” ― Markus Zusak, The Book Thief "

             ]
    romance = [
        "“He's like a drug for you, Bella.” ",
        "“Some women choose to follow men, and some women choose to follow their dreams. If you're wondering which way to go, remember that your career will never wake up and tell you that it doesn't love you anymore.” ― Lady Gaga ",
        " “The very essence of romance is uncertainty.” ― Oscar Wilde",
        "“If you love somebody, let them go, for if they return, they were always yours. If they don't, they never were.” ― Kahlil Gibran ",
        "“When love is not madness it is not love.” ― Pedro Calderon de la Barca ",
        "“True love is rare, and it's the only thing that gives life real meaning.” ― Nicholas Sparks, Message in a Bottle ",
        "“I was smiling yesterday,I am smiling today and I will smile tomorrow.Simply because life is too short to cry for anything.”― Santosh Kalwar, Quote Me Everyday ",
        "“Never close your lips to those whom you have already opened your heart.” ― Charles Dickens "]

    if topic_response == "humor" or 1:
        return choice(humor)
    elif topic_response == "religion" or 2:
        return choice(religion)
    elif topic_response == "wisdom" or 3:
        return choice(wisdom)
    elif topic_response == "death" or 4:
        return choice(death)
    elif topic_response == "romance" or 5:
        return choice(romance)
    else:
        return "Please enter a quote section or 'done' to leave"
