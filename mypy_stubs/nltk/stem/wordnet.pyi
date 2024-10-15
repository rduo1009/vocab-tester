from _typeshed import Incomplete

class WordNetLemmatizer:
    def morphy(
        self,
        form: Incomplete,
        pos: Incomplete | None = None,
        check_exceptions: bool = True,
    ) -> Incomplete: ...
    def lemmatize(self, word: str, pos: str = "n") -> str: ...
