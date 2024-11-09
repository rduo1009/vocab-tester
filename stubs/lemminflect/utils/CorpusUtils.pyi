import re

def loadNLTKCorpus(corp_fn: str, max_chars: int = int(1e12)) -> list[str]: ...

is_ascii_regex: re.Pattern[str]

def isASCIIWord(word: str) -> bool: ...
