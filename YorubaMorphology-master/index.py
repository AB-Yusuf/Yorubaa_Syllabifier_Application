import re
import string
from syllabicator import *


def pre_process_word(sentence):
    sentence = re.sub(r'\d+', '', sentence)  # remove digits
    sentence = sentence.translate(sentence.maketrans('', '', string.punctuation))  # remove punctuation
    return sentence.strip()


file = 'news_site.txt'

r = open(file, 'r')
w = open(file.replace('.', '_syllables.'), 'w')
e = open(file.replace('.', '_errors.'), 'w')

print('----STARTING-----')

while True:
    line = r.readline()
    if not line:
        break
    sentence = pre_process_word(line)
    for word in sentence.split(' '):
        if word:
            try:
                syllable = syllabicator_i.syllabicate(word)
                w.write(word + " - " + syllable + "\n")
            except ValueError:
                e.write(word + "\n")
                print("An exception occurred with ", word)

    print('----DONE-----')

r.close()
w.close()
