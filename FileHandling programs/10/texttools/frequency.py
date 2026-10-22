# texttools/frequency.py
def word_frequency(tokens):
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq