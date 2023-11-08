from src.funnygpt import functions

def main():
    print(functions.gptchat())
    print(functions.gptchat(subject="what is your name"))
    print(functions.gptchat("joke"))
    print(functions.gptchat("joke", "software engineers"))
    print(functions.gptchat("haiku"))
    print(functions.gptchat("haiku", "software engineers"))
    print(functions.gptchat("compliment"))
    print(functions.gptchat("compliment", "software engineers"))
    print(functions.gptchat("email"))
    print(functions.gptchat("email", "software engineers"))
    # functions.haiku()
    # functions.compliment()
    # functions.email()

    # functions.joke("software engineers")
    # functions.haiku("carbon dioxide")
    # functions.compliment("mustache")
    # functions.email("tell my professor I can't come to class today because")



if __name__ == "__main__":
    main()