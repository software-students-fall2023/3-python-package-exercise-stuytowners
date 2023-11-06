import openai

def llm(question):
   response = openai.Completion.create(
   engine = "text-davinci-003",
   prompt = question,
   max_tokens=200,
   temperature=0.99
   )
   answer = response.choices[0].text.strip()

   return answer

preset = "You are the most chill cs professor in the world, Professor Foo Barstein. You are talking to me, a student in your class."

def gptchat(type=None, subject=None, preset=preset):
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
    else:
        if (subject):
            response=llm(preset + subject)
        else:
            response=llm(preset + "say something random")
    print(response)

def cowtalk():
    pass

def onewordperline():
    pass

def changepreset():
    pass


