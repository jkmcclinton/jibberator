import sqlite3
from sqlite3 import Error

# from languages import LANGUAGES
from typing import List

from api.components.logging import logger
from api.components.enumerators import Language

SQL_PATH = "./data/dictionary.db"


class SqlInterface:
    def __init__(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect(SQL_PATH)
            logger.debug("Connection to SQLite DB successful.")
        except Error as e:
            logger.exception(e)

    def __del__(self):
        self.connection.close()

    def query(self, lang: Language, word: str) -> dict:
        """Pulls a word from a table"""
        sql = f"SELECT * FROM {lang} WHERE text = '{word}'"
        cursor = self.connection.cursor()

        try:
            response = cursor.execute(sql)
            return response.fetchone()
        except Exception as error:
            logger.exception(error)
            return {}

    def get_all(self, lang: Language) -> List[dict]:
        """Get all words in language from DB"""
        sql = f"""SELECT * FROM {lang}"""
        cursor = self.connection.cursor()

        try:
            response = cursor.execute(sql)
            return response.fetchall()
        except Exception as error:
            logger.exception(error)
            return []

    def write(self, lang: Language, words: List[dict]) -> bool:
        """Writes a record into a table"""

        sql = f"""INSERT INTO \n\t{lang} ( %fields% ) \nVALUES \n\t%values%;"""
        cursor = self.connection.cursor()

        fields = [f"`{f}`" for f in words[0].keys()]
        values = [str(tuple([str(v) for v in word.values()])) for word in words]

        sql = sql.replace("%fields%", ", ".join(fields)).replace("%values%", ",\n\t".join(values))
        logger.debug(f"SQL Query: \n{sql}")

        try:
            cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as error:
            logger.exception(error)
            return False

    def update(self, lang: Language, word: dict) -> bool:
        """Update fields of a word"""

        sql = f"""UPDATE {lang} SET ( %fields% ) WHERE text = '{word['text']}'"""
        logger.debug(f"SQL Query: \n{sql}")
        del word["text"]

        expressions = []
        for field, value in word.values():
            expressions.append(f"{field} = '{value}'")

        sql = sql.replace("%fields%", ", ".join(expressions))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)

            return True
        except Exception as error:
            logger.exception(error)
            return False


SQL_CLIENT = SqlInterface()
