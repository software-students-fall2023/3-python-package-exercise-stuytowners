from my_module import functions

def main():
    functions.joke()
    functions.haiku()
    functions.compliment()
    functions.email()

    functions.joke("software engineers")
    functions.haiku("carbon dioxide")
    functions.compliment("mustache")
    functions.email("tell my professor I can't come to class today because")



if __name__ == "__main__":
    main()