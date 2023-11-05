import pyttsx3
name = input("what's your name? \n")
engine = pyttsx3.init()
engine.say(f" {name}")
engine.runAndWait()
print("done")

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

