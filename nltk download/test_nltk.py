import nltk
from nltk.tokenize import word_tokenize

# Sample text
text = "Hello! Welcome to learning Natural Language Processing with NLTK."

# Break the sentence into individual words (tokens)
tokens = word_tokenize(text)

print("Tokens:", tokens)