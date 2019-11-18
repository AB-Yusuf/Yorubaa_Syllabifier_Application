import unicodedata
import re


_V = {'a', 'e', 'ẹ', 'i', 'o', 'ọ', 'u', 'à', 'è', '̀ẹ', 'ì', 'ò', '̀ọ', 'ù', 'á', 'é', '́ẹ', 'í', 'ó', '́ọ', 'ú'}
V = {'a', 'e', 'ẹ', 'i', 'o', 'ọ', 'u', 'à', 'è', 'ḕ', 'ì', 'ò', 'ṑ', 'ù', 'á', 'é', 'ḗ', 'í', 'ó', 'ṓ', 'ú',
     'A', 'Ó', 'À', 'Ṓ', 'Ḕ', 'È', 'O', 'I', 'Ḗ', 'Á', 'Ṑ', 'Í', 'Ì', 'Ẹ', 'E', 'U', 'É', 'Ú', 'Ò', 'Ọ', 'Ù'}

_Vn = {'an', 'ẹn', 'in', 'ọn', 'un', 'àn', '̀ẹn', 'ìn', '̀ọn', 'ùn', 'án', '́ẹn', 'ín', '́ọn', 'ún'}
Vn = {'an', 'ẹn', 'in', 'ọn', 'un', 'àn', 'ḕn', 'ìn', 'ṑn', 'ùn', 'án', 'ḗn', 'ín', 'ṓn', 'ún',
      'ÚN', 'UN', 'ÍN', 'ÁN', 'ÀN', 'ÌN', 'ẸN', 'ÙN', 'ḖN', 'ṒN', 'ỌN', 'AN', 'ṐN', 'IN', 'ḔN'}

N = {'m', 'n', 'ṁ', 'ǹ', 'ḿ', 'ń',
     'Ǹ', 'M', 'N', 'Ḿ', 'Ṁ', 'Ń'}

C = {'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ṣ', 't', 'w', 'y',
     'G', 'Y', 'D', 'L', 'M', 'W', 'F', 'N', 'S', 'R', 'Ṣ', 'J', 'P', 'K', 'H', 'B', 'T'}
D = {'gb', 'GB'}

yo_to_la = {'̀ẹ': 'ḕ', '̀ọ': 'ṑ', '́ẹ': 'ḗ', '́ọ': 'ṓ', '̀m': 'ṁ', '-': '',
            'ẹ̀': 'ḕ', 'ọ̀': 'ṑ', 'ẹ́': 'ḗ', 'ọ́': 'ṓ', 'm̀': 'ṁ'}
# la_to_ya = {'ḕ': '̀ẹ', 'ṑ': '̀ọ', 'ḗ': '́ẹ', 'ṓ': '́ọ'}
la_to_ya = {'ḕ': 'ẹ̀', 'ṑ': 'ọ̀', 'ḗ': 'ẹ́', 'ṓ': 'ọ́'}


def syllabicate(word):
    word = multi_replace(word, yo_to_la)

    syllable = ''
    while len(word) >= 1:
        if len(word) > 3:
            if word[-4:-2] in D and word[-2:] in Vn:  # DVn
                syllable = word[-4:] + ' ' + syllable
                word = word[0:-4]
            else:
                if word[-3:-1] in D and word[-1] in V:  # DV Structure
                    syllable = word[-3:] + ' ' + syllable
                    word = word[0:-3]

                elif word[-3] in C and word[-2:] in Vn:  # CVn Structure
                    syllable = word[-3:] + ' ' + syllable
                    word = word[0:-3]
                else:
                    if word[-2] in C and word[-1] in V:  # CV Structure
                        syllable = word[-2:] + ' ' + syllable
                        word = word[0:-2]
                    elif word in Vn:  # Vn Structure
                        syllable = word[-2:] + ' ' + syllable
                        word = word[0:-2]
                    else:
                        if word[-1] in V:  # V Structure
                            syllable = word[-1:] + ' ' + syllable
                            word = word[0:-1]
                        elif word[-1] in N:
                            syllable = word[-1:] + ' ' + syllable
                            word = word[0:-1]
                        else:
                            raise ValueError('An error occurred with last char')

        elif len(word) == 3:
            if word[-3:-1] in D and word[-1] in V:  # DV Structure
                syllable = word[-3:] + ' ' + syllable
                word = word[0:-3]

            elif word[-3] in C and word[-2:] in Vn:  # CVn Structure
                syllable = word[-3:] + ' ' + syllable
                word = word[0:-3]
            else:
                if word[-2] in C and word[-1] in V:  # CV Structure
                    syllable = word[-2:] + ' ' + syllable
                    word = word[0:-2]
                elif word in Vn:  # Vn Structure
                    syllable = word[-2:] + ' ' + syllable
                    word = word[0:-2]
                else:
                    if word[-1] in V:  # V Structure
                        syllable = word[-1:] + ' ' + syllable
                        word = word[0:-1]
                    elif word[-1] in N:
                        syllable = word + ' ' + syllable
                        word = word[0:-1]
                    else:
                        raise ValueError('An error occurred with last char')

        elif len(word) == 2:
            if word[-2] in C and word[-1] in V:  # CV Structure
                syllable = word[-2:] + ' ' + syllable
                word = word[0:-2]
            elif word in Vn:  # Vn Structure
                syllable = word[-2:] + ' ' + syllable
                word = word[0:-2]
            else:
                if word[-1] in V:  # V Structure
                    syllable = word[-1:] + ' ' + syllable
                    word = word[0:-1]
                elif word[-1] in N:
                    syllable = word[-1:] + ' ' + syllable
                    word = word[0:-1]
                else:
                    raise ValueError('An error occurred with last char')

        else:
            if word[-1] in V:  # V Structure
                syllable = word[-1:] + ' ' + syllable
                word = word[0:-1]
            elif word[-1] in N:
                syllable = word[-1:] + ' ' + syllable
                word = word[0:-1]
            else:
                raise ValueError('An error occurred with last char')

    return multi_replace(syllable, la_to_ya)


def multi_replace(string, replacements):
    """
    Given a string and a replacement map, it returns the replaced string.
    :param str string: string to execute replacements on
    :param dict replacements: replacement dictionary {value to find: value to replace}
    :rtype: str
    """
    # Place longer ones first to keep shorter substrings from matching where the longer ones should take place
    # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against the string 'hey abc', it should produce
    # 'hey ABC' and not 'hey ABc'
    substrs = sorted(replacements, key=len, reverse=True)

    # Create a big OR regex that matches any of the substrings to replace
    regexp = re.compile('|'.join(map(re.escape, substrs)))

    # For each match, look up the new string in the replacements
    return regexp.sub(lambda match: replacements[match.group(0)], string)







