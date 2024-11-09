import threading
from collections.abc import Generator

from _typeshed import Incomplete

from nltk.draw.table import Table as Table
from nltk.draw.util import ShowText as ShowText

TKINTER: bool
TclError = ValueError

class Package:
    id: Incomplete
    name: Incomplete
    subdir: Incomplete
    url: Incomplete
    size: Incomplete
    unzipped_size: Incomplete
    checksum: Incomplete
    svn_revision: Incomplete
    copyright: Incomplete
    contact: Incomplete
    license: Incomplete
    author: Incomplete
    filename: Incomplete
    unzip: Incomplete
    def __init__(
        self,
        id: Incomplete,
        url: Incomplete,
        name: Incomplete | None = None,
        subdir: str = "",
        size: Incomplete | None = None,
        unzipped_size: Incomplete | None = None,
        checksum: Incomplete | None = None,
        svn_revision: Incomplete | None = None,
        copyright: str = "Unknown",
        contact: str = "Unknown",
        license: str = "Unknown",
        author: str = "Unknown",
        unzip: bool = True,
        **kw: Incomplete,
    ) -> None: ...
    @staticmethod
    def fromxml(xml: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...

class Collection:
    id: Incomplete
    name: Incomplete
    children: Incomplete
    packages: Incomplete
    def __init__(
        self,
        id: Incomplete,
        children: Incomplete,
        name: Incomplete | None = None,
        **kw: Incomplete,
    ) -> None: ...
    @staticmethod
    def fromxml(xml: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...

class DownloaderMessage: ...

class StartCollectionMessage(DownloaderMessage):
    collection: Incomplete
    def __init__(self, collection: Incomplete) -> None: ...

class FinishCollectionMessage(DownloaderMessage):
    collection: Incomplete
    def __init__(self, collection: Incomplete) -> None: ...

class StartPackageMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class FinishPackageMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class StartDownloadMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class FinishDownloadMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class StartUnzipMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class FinishUnzipMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class UpToDateMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class StaleMessage(DownloaderMessage):
    package: Incomplete
    def __init__(self, package: Incomplete) -> None: ...

class ErrorMessage(DownloaderMessage):
    package: Incomplete
    message: Incomplete
    def __init__(self, package: Incomplete, message: Incomplete) -> None: ...

class ProgressMessage(DownloaderMessage):
    progress: Incomplete
    def __init__(self, progress: Incomplete) -> None: ...

class SelectDownloadDirMessage(DownloaderMessage):
    download_dir: Incomplete
    def __init__(self, download_dir: Incomplete) -> None: ...

class Downloader:
    INDEX_TIMEOUT: Incomplete
    DEFAULT_URL: str
    INSTALLED: str
    NOT_INSTALLED: str
    STALE: str
    PARTIAL: str
    def __init__(
        self,
        server_index_url: Incomplete | None = None,
        download_dir: Incomplete | None = None,
    ) -> None: ...
    def list(
        self,
        download_dir: Incomplete | None = None,
        show_packages: bool = True,
        show_collections: bool = True,
        header: bool = True,
        more_prompt: bool = False,
        skip_installed: bool = False,
    ) -> None: ...
    def packages(self) -> Incomplete: ...
    def corpora(self) -> Incomplete: ...
    def models(self) -> Incomplete: ...
    def collections(self) -> Incomplete: ...
    def incr_download(
        self,
        info_or_id: Incomplete,
        download_dir: Incomplete | None = None,
        force: bool = False,
    ) -> Generator[Incomplete, Incomplete, None]: ...
    def download(
        self,
        info_or_id: Incomplete | None = None,
        download_dir: Incomplete | None = None,
        quiet: bool = False,
        force: bool = False,
        prefix: str = "[nltk_data] ",
        halt_on_error: bool = True,
        raise_on_error: bool = False,
        print_error_to: Incomplete = ...,
    ) -> Incomplete: ...
    def is_stale(
        self, info_or_id: Incomplete, download_dir: Incomplete | None = None
    ) -> Incomplete: ...
    def is_installed(
        self, info_or_id: Incomplete, download_dir: Incomplete | None = None
    ) -> Incomplete: ...
    def clear_status_cache(self, id: Incomplete | None = None) -> None: ...
    def status(
        self, info_or_id: Incomplete, download_dir: Incomplete | None = None
    ) -> Incomplete: ...
    def update(
        self, quiet: bool = False, prefix: str = "[nltk_data] "
    ) -> None: ...
    def index(self) -> Incomplete: ...
    def info(self, id: Incomplete) -> Incomplete: ...
    def xmlinfo(self, id: Incomplete) -> Incomplete: ...
    url: Incomplete
    def default_download_dir(self) -> Incomplete: ...
    download_dir: Incomplete

class DownloaderShell:
    def __init__(self, dataserver: Incomplete) -> None: ...
    def run(self) -> None: ...

class DownloaderGUI:
    COLUMNS: Incomplete
    COLUMN_WEIGHTS: Incomplete
    COLUMN_WIDTHS: Incomplete
    DEFAULT_COLUMN_WIDTH: int
    INITIAL_COLUMNS: Incomplete
    def __init__(
        self, dataserver: Incomplete, use_threads: bool = True
    ) -> None: ...
    def destroy(self, *e: Incomplete) -> None: ...
    def mainloop(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    HELP: Incomplete
    def help(self, *e: Incomplete) -> None: ...
    def about(self, *e: Incomplete) -> None: ...
    class _DownloadThread(threading.Thread):
        data_server: Incomplete
        items: Incomplete
        lock: Incomplete
        message_queue: Incomplete
        abort: Incomplete
        def __init__(
            self,
            data_server: Incomplete,
            items: Incomplete,
            lock: Incomplete,
            message_queue: Incomplete,
            abort: Incomplete,
        ) -> None: ...
        def run(self) -> None: ...

def md5_hexdigest(file: Incomplete) -> Incomplete: ...
def unzip(
    filename: Incomplete, root: Incomplete, verbose: bool = True
) -> None: ...
def build_index(root: Incomplete, base_url: Incomplete) -> Incomplete: ...

download: Incomplete

def download_shell() -> None: ...
def download_gui() -> None: ...
def update() -> None: ...
