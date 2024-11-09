from _typeshed import Incomplete

windowTitle: str
initialFind: str
initialRepl: str
initialText: str
images: Incomplete
colors: Incomplete
emphColors: Incomplete
fieldParams: Incomplete
textParams: Incomplete

class Zone:
    image: Incomplete
    imageDimmed: Incomplete
    img: Incomplete
    fld: Incomplete
    txt: Incomplete
    def __init__(
        self,
        image: Incomplete,
        initialField: Incomplete,
        initialText: Incomplete,
    ) -> None: ...
    def initScrollText(
        self, frm: Incomplete, txt: Incomplete, contents: Incomplete
    ) -> None: ...
    colorCycle: Incomplete
    def refresh(self) -> None: ...

class FindZone(Zone):
    def addTags(self, m: Incomplete) -> None: ...
    rex: Incomplete
    rexSel: Incomplete
    def substitute(self, *args: Incomplete) -> None: ...

class ReplaceZone(Zone):
    def addTags(self, m: Incomplete) -> None: ...
    diff: int
    repl: Incomplete
    def substitute(self) -> None: ...

def launchRefresh(_: Incomplete) -> None: ...
def app() -> None: ...
