
from api.components.enumerators import Language


def phonetic_translate(word: str, source: Language, dest: Language) -> str:
    """"""
    pass


def translate(passage: str, source: Language, dest: Language) -> str:
    """Translates a block of text using phonetic based translation"""
    words = passage.split(" ")
    translated = []

    for word in words:
        translated.append(phonetic_translate(word, source, dest))

    return " ".join(translated)