# main.py
from texttools import cleaning, tokenization, frequency

text = "  hello world hello python  "
cleaned = cleaning.remove_extra_spaces(text)
tokens = tokenization.tokenize(cleaned)
print("Frequency:", frequency.word_frequency(tokens))