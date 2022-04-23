from enum import Enum


class OutputFriendly(Enum):
    """Formats internal enumerations for better output in logging.
    Must include an `unknown` field for error handling."""

    def __str__(self):
        return self.value

    @classmethod
    def _missing_(cls, value):
        """
        Final fail safe before raising a ValueError; if requested
        enum value is not defined, then default to a catch-all value.
        This makes doing OutputFriendly(value) always return a value.
        """
        return cls.unknown


class OxfordEndpoint(OutputFriendly):
    entries = "/entries"


class Language(OutputFriendly):
    unknown = "unwn"
    english_uk = "en-gb"
    english_us = "en-us"
    english = "en"
    arabic = "ar"
    chinese = "zh"
    farsi = "fa"
    french = "fr"
    georgian = "ka"
    german = "de"
    greek = "el"
    gujarti = "gu"
    hausa = "ha"
    hindi = "hi"
    igbo = "ig"
    indonesian = "id"
    italian = "xh"
    latvian = "lv"
    malay = "ms"
    marathi = "mr"
    isi_xhosa = "xh"
    portugese = "pt"
    quechua = "qu"
    romanian = "ro"
    russian = "ru"
    setswana = "tn"
    spanish = "es"
    swahili = "sw"
    tajik = "tg"
    tamil = "ta"
    tatar = "tt"
    telugu = "te"
    tok_pisin = "tpi"
    turkmen = "tk"
    urdu = "ur"
    yoruba = "yo"


"""Languages allowed for translation"""
TRANSLATION_AVAILABLE = [
    Language.english_uk,
    Language.english_us,
    Language.french,
    Language.german,
    Language.hindi,
    Language.latvian,
    Language.romanian,
    Language.swahili,
    Language.tamil,
    Language.spanish,
]
