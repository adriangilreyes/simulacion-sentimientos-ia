from textblob import TextBlob

phrase = "Hoy me siento cansado"

blob = TextBlob(phrase)

print(blob.sentiment)