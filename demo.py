from my_module import functions

def main():
    functions.gptchat()
    functions.gptchat(subject="what is your name")
    functions.gptchat("joke")
    functions.gptchat("joke", "software engineers")
    functions.gptchat("haiku")
    functions.gptchat("haiku", "software engineers")
    functions.gptchat("compliment")
    functions.gptchat("compliment", "software engineers")
    functions.gptchat("email")
    functions.gptchat("email", "software engineers")
    # functions.haiku()
    # functions.compliment()
    # functions.email()

    # functions.joke("software engineers")
    # functions.haiku("carbon dioxide")
    # functions.compliment("mustache")
    # functions.email("tell my professor I can't come to class today because")



if __name__ == "__main__":
    main()