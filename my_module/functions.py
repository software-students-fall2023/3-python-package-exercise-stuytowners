from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003")

preset = "You are the most chill cs professor in the world, Professor Foo Barstein. You are talking to me, a student in your class."

def gptchat(type, subject=None, preset=preset):
    if (type=="joke"):
        if (subject):
            response=llm(preset + "tell me a funny joke about " + subject)
        else:
            response=llm(preset + "tell me a funny joke")
    elif (type=="haiku"):
        if (subject):
            response=llm(preset + "tell me a haiku about " + subject)
        else:
            response=llm(preset + "tell me a haiku")
    elif (type=="compliment"):
        if (subject):
            response=llm(preset + "tell me a compliment about " + subject)
        else:
            response=llm(preset + "tell me a compliment")
    elif (type=="email"):
        if (subject):
            response=llm(preset + "write an email about " + subject)
        else:
            response=llm(preset + "write a random email to send to my boss")
    print(response)

def cowtalk():
    pass

def onewordperline():
    pass

def changepreset():
    pass


