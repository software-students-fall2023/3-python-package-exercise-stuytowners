from src.funnygpt import functions

def main():
    askName=functions.gptchat(subject="what is your name")
    test_joke=functions.gptchat("joke", "software engineers")
    test_haiku=functions.gptchat("haiku", "software engineers")
    test_compliments=functions.gptchat("compliments", "software engineers")
    test_cowtalk=functions.cowtalk(test_joke)
    test_email=functions.gptchat("email","to Professor Boo")
    test_owpl=functions.onewordperline("hello world")
    functions.changepreset()
    test_gpt_2=functions.gptchat("joke", "Thanksgiving")
    #print(askName)
    #print(test_joke)
    #print(test_haiku)
    #print(test_compliments)
    #print(test_cowtalk)
    #print(test_email)
    #print(test_owpl)
    #print(test_gpt_2)
    # functions.haiku()
    # functions.compliment()
    # functions.email()

    # functions.joke("software engineers")
    # functions.haiku("carbon dioxide")
    # functions.compliment("mustache")
    # functions.email("tell my professor I can't come to class today because")



if __name__ == "__main__":
    main()