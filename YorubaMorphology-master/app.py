import unicodedata
import re
from syllabicator import *

print(syllabicator_i.syllabicate('la'))
print(syllabicator_i.syllabicate('gba'))
print(syllabicator_i.syllabicate('fun'))
print(syllabicator_i.syllabicate('gbafun'))

print(syllabicator_i.syllabicate('tẹtan'))
print(syllabicator_i.syllabicate('sunkanmi'))
print(syllabicator_i.syllabicate('ọkùnrin'))
print(syllabicator_i.syllabicate('agbára'))
# print(syllabicator('m̀ẹwàá'))
print(syllabicator_i.syllabicate('Mọkànlá'))
print("--------")
print(syllabicator_i.syllabicate('mẹ̀wàá'))

#
# single_char = '̀m'
# multiple_chars = '\N{LATIN SMALL LETTER E WITH DOT BELOW}\N{COMBINING ACUTE ACCENT}'
# print('length of first string=', len(single_char), single_char)
# print('length of second string=', len(multiple_chars), multiple_chars)
# normalized_string = unicodedata.normalize('NFKC', single_char)
# print('length of normalized string=', len(normalized_string),normalized_string)
# print(unicodedata.name(single_char))
# print(ord(single_char))

string = 'ìhámọ́'
dict = {'̀ẹ':'ḕ','̀ọ':'ṑ','́ẹ':'ḗ','́ọ':'ṓ','ẹ̀':'ḕ','ọ̀':'ṑ','ẹ́':'ḗ','ọ́': 'ṓ'}
print(syllabicator_i.multi_replace(string,dict))
# print(syllabicator_i.syllabicate(string))
# A = ['m', 'n', 'ṁ', 'ǹ', 'ḿ', 'ń', 'Ǹ', 'M', 'N', 'Ḿ', 'Ṁ', 'Ń']
# print(unicodedata.name(A[4]))

try:
  print(syllabicator_i.syllabicate(string))
except ValueError:
  print("An exception occurred")



print(syllabicator_i.syllabicate('àlàáfíà'))







