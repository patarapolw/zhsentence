import re
from wordfreq import word_frequency


def zh_split(value):
    return [x.strip() for x in re.split(r'[,，\n]', value) if x.strip()]


def get_freq(word):
    return word_frequency(word.strip(), 'zh') * 10 ** 6
