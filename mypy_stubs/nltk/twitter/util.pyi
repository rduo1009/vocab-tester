from _typeshed import Incomplete

def credsfromfile(
    creds_file: Incomplete | None = None,
    subdir: Incomplete | None = None,
    verbose: bool = False,
) -> Incomplete: ...

class Authenticate:
    creds_file: str
    creds_fullpath: Incomplete
    oauth: Incomplete
    twitter_dir: Incomplete
    creds_subdir: Incomplete
    def __init__(self) -> None: ...
    def load_creds(
        self,
        creds_file: Incomplete | None = None,
        subdir: Incomplete | None = None,
        verbose: bool = False,
    ) -> Incomplete: ...

def add_access_token(creds_file: Incomplete | None = None) -> None: ...
def guess_path(pth: Incomplete) -> Incomplete: ...
