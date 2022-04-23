import os
import json
import requests

from api.components.enumerators import OxfordEndpoint, Language
from api.components.logging import logger

CLIENT_ID = os.environ.get("OXFORD_ID", "")
CLIENT_SECRET = os.environ.get("OXFORD_CLIENT", "")
OXFORD_URL = "https://od-api.oxforddictionaries.com/api/v2"


class OxfordInterface:

    def __init__(self):
        self.headers = {"app_id": CLIENT_ID, "app_key": CLIENT_SECRET}

    def fetch(self, endpoint: OxfordEndpoint, language: Language, data: str) -> dict:

        if self.headers is None:
            logger.warning("Not authorized to perform Oxford API call.")
            return {}

        url = f"{OXFORD_URL}{endpoint}/{language}/{data}"
        logger.info(f"Oxford::fetching: {url}")

        try:
            response = requests.get(url)

            logger.info(f"Oxford::response: [{response.status_code}] {response.text}")

            if not response.ok:
                return {}

            return response.json()
        except Exception as error:
            logger.exception(error)
            return {}


OXFORD_CLIENT = OxfordInterface()
