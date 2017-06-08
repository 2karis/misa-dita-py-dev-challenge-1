import re
def uppercase(matchobj):
    return matchobj.group(0).upper()

def capitalize(s):
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, s)

words = input()
words.capitalize()
words.replace(".", ". ")
words.replace(" .", ".")
words = words.replace(",", ", ")
words = words.replace(".", ". ")
words = words.replace("!", "! ")
words = words.replace(",", ", ")
words = words.replace(",", ", ")
words = words.replace(":", ": ")
words = words.replace(";", "; ")
words = capitalize(words)

words = ' '.join(words.split())

print(words)
