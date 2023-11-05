from textblob import TextBlob

text = "welcome to my wrks"

tb = TextBlob(text)

correct_text = tb.correct()

print(correct_text)