# string_utils.py
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def reverse_string(s):
    return s[::-1]

def check_palindrome(s):
    return s == s[::-1]

def count_words(s):
    return len(s.split())

def remove_spaces(s):
    return "".join(s.split())