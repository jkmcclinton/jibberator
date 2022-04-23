from dataclasses import dataclass
from typing import List


@dataclass
class Word:
    text:str
    phonetics:str
    syllables:List[str]
