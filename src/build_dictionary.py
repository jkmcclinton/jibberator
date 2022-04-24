"""
Builds local database with all possible words. This should be a one time operation
and forms the basis of all future operations of defining words with pronunciation data.
Project root must be in PYTHONPATH.
"""
from api.components.decorators import time_segment
from api.components.enumerators import Language
from api.components.logging import logger
from api.interfaces.sql import SQL_CLIENT

EN_WORDS = "./data/en_us.txt"

LONGEST = 15
"""The length of the longest word in file (ENGLISH)"""

def get_word_list() -> list:
    with open(EN_WORDS) as f:
        result = f.readlines()

    return list({word.strip() for word in result})


def save_to_database(words: list):
    longest = 0
    converted = []

    for word in words:
        if len(word) > longest:
            longest = len(word)

        converted.append({
            "text": word,
            "phonetics": None,
            "syllables": None,
        })

    logger.info(f"Longest word: {longest}")
    SQL_CLIENT.write(Language.english, converted)

@time_segment
def main():
    words = get_word_list()
    logger.debug(f"Pulled {len(words)} word(s) from English list.")

    save_to_database(words)


if __name__ == '__main__':
    main()
