# -*- coding: utf-8 -*-
from .cleaner import italian_cleaners
from .gruut_wrapper import Gruut

# Italian vowels using Unicode escape sequences
italian_vowels = set('aeiou' + 
                         '\u00E0'  # �
                         '\u00E8'  # �
                         '\u00E9'  # �
                         '\u00EC'  # �
                         '\u00ED'  # �
                         '\u00EE'  # �
                         '\u00F2'  # �
                         '\u00F3'  # �
                         '\u00F9'  # �
                         '\u00FA'  # �
                        )
def remove_consecutive_consonants(input_str):
    result = []
    prev_char = ''
    count = 0

    for char in input_str:
        if char == prev_char and char not in italian_vowels:
            count += 1
        else:
            if count < 3:
                result.extend([prev_char] * count)
            count = 1
            prev_char = char

    if count < 3:
        result.extend([prev_char] * count)

    return ''.join(result)

def it2ipa(text):
    e = Gruut(language="it", keep_puncs=True, keep_stress=True, use_espeak_phonemes=True)
    # text = italian_cleaners(text)
    phonemes = e.phonemize(text, separator="")
    # print(phonemes)
    phonemes = remove_consecutive_consonants(phonemes)
    # print(phonemes)
    return phonemes