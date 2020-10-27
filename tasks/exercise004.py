# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.
import re

def pig_it(text):
    text = re.sub(r'\w+', lambda w: w.group()[1:] + w.group()[0] + 'ay', text)
    return text
