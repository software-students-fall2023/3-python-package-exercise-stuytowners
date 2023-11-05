from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003")

preset = "You are the most chill cs professor in the world, Professor Foo Barstein. You are talking to me, a student in your class."

def joke(subject=None):
    if (subject):
        response=llm(preset + "tell me a funny joke about " + subject)
    else:
        response=llm(preset + "tell me a funny joke")

    print(response)

def haiku(subject=None):
    if (subject):
        response=llm(preset + "tell me a haiku about " + subject)
    else:
        response=llm(preset + "tell me a haiku")

    print(response)

def compliment(subject=None):
    if (subject):
        response=llm(preset + "tell me a compliment about " + subject)
    else:
        response=llm(preset + "tell me a compliment")

    print(response)

def email(subject=None):
    if (subject):
        response=llm(preset + "write an email about " + subject)
    else:
        response=llm(preset + "write a random email to send to my boss")

    print(response)

