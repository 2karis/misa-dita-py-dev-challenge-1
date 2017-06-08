import re
def uppercase(matchobj):
    return matchobj.group(0).upper()

def capitalize(s):
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, s)

def replace(matchobj):
    return matchobj.group(0) + ' ';

def space(s):
    return re.sub('[.?!,!:;]', replace, s) 
words = input()

words = space(words)
words = capitalize(words)

words = ' '.join(words.split())

print(words)

