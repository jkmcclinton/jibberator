"""
Builds local database with all possible words. This should be a one time operation
and forms the basis of all future operations of defining words with pronunciation data.
Project root must be in PYTHONPATH.
"""

import json

from api.components.logging import logger

EN_WORDS = "./data/en_us.txt"

def get_word_list() -> list:
    with open(EN_WORDS) as f:
        result = f.readlines()

    return [word.replace("\n", "") for word in result]


def save_to_database(words: list):
    pass


def main():
    words = get_word_list()
    logger.debug(f"Pulled {len(words)} word(s) from English list.")

    save_to_database(words)


if __name__ == '__main__':
    main()
