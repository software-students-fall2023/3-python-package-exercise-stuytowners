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

def cowtalk(response):
    words = response.split()
    moo_response = " ".join(" ".join(words[i:i+2]) for i in range(0, len(words), 2))
    print(moo_response)

def onewordperline():
    words = response.split()  # Split the response into words
    max_word_length = max(len(word) for word in words)

    for i in range(max_word_length):
        for word in words:
            if i < len(word):
                print(word[i], end=' ')
            else:
                print('  ', end=' ')  # Print two spaces for alignment
        print()

def changepreset():
    new_preset = input("Enter the new preset: ")
    global preset  # Use the 'preset' variable defined outside the function
    preset = new_preset


