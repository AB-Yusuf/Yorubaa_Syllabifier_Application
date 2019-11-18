# K = ['b', 'd', 'f', 'g', 'gb', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 's'̣, 't', 'w', 'y']
# V = ['a','e','ẹ','i','o','ọ','u','à','è','̀ẹ','ì','ò','̀ọ','ù','á','é','́ẹ',í','ó','́ọ','ú']
# N = ['am','ẹn','in','ọn','un','àn','̀ẹn',ìn','̀ọn',ùn','án','́ẹn','ín','́ọn','ún']
# S = ['m','n','̀m','̀n','́m','́n']


V = ['a', 'e', 'ẹ', 'i', 'o', 'ọ', 'u', 'à', 'è', '̀ẹ', 'ì', 'ò', '̀ọ', 'ù', 'á', 'é', '́ẹ', 'í', 'ó', '́ọ', 'ú']
Vn = ['an', 'ẹn', 'in', 'ọn', 'un', 'àn', '̀ẹn', 'ìn', '̀ọn', 'ùn', 'án', '́ẹn', 'ín', '́ọn', 'ún']
N = ['m', 'n', '̀m', '̀n', '́m', '́n']
C = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ṣ', 't', 'w', 'y']
D = ['gb']


def syllabicator_r(word):
    syllable = ''

    if len(word) > 3:
        if word[-4:-2] in D and word[-2:] in Vn:  # DVn
            syllable = word + ' ' + syllable
            word = word[0:4]
        else:
            syllable = syllabicator_r(word[-3:]) + ' ' + syllable
            word = word[0:-3]

    if len(word) == 3:
        if word[-3:-1] in D and word[-1] in V:  # DV Structure
            syllable = word + ' ' + syllable
            word = word[0:-3]

        elif word[-3] in C and word[-2:] in Vn:  # CVn Structure
            syllable = word + ' ' + syllable
            word = word[0:-3]
        else:
            syllable = syllabicator_r(word[-2:]) + ' ' + syllable
            word = word[0:-2]

    if len(word) == 2:
        if word[-2] in C and word[-1] in V:  # CV Structure
            syllable = word + ' ' + syllable
            word = word[0:-2]
        elif word in Vn:  # Vn Structure
            syllable = word + ' ' + syllable
            word = word[0:-2]
        else:
            syllable = syllabicator_r(word[-1:]) + ' ' + syllable
            word = word[0:-1]

    if len(word) == 1:
        if word[-1] in V: # V Structure
            syllable = word + ' ' + syllable
            word = word[0:-1]
        elif word[-1] in N:
            syllable = word + ' ' + syllable
            word = word[0:-1]
        else:
            raise ValueError('An error occurred with last char')

    if len(word) < 1:
        return syllable

    return syllabicator_r(word) + syllable



print(syllabicator_r('la'))
print(syllabicator_r('gba'))
print(syllabicator_r('fun'))
print(syllabicator_r('gbafun'))

print(syllabicator_r('tẹtan'))
print(syllabicator_r('sunkanmi'))
print(syllabicator_r('agbára'))





