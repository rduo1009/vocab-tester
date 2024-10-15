from tkinter import Frame

from _typeshed import Incomplete

class MultiListbox(Frame):
    FRAME_CONFIG: Incomplete
    LABEL_CONFIG: Incomplete
    LISTBOX_CONFIG: Incomplete
    def __init__(
        self,
        master: Incomplete,
        columns: Incomplete,
        column_weights: Incomplete | None = None,
        cnf: Incomplete = {},
        **kw: Incomplete,
    ) -> None: ...
    @property
    def column_names(self) -> Incomplete: ...
    @property
    def column_labels(self) -> Incomplete: ...
    @property
    def listboxes(self) -> Incomplete: ...
    def select(
        self,
        index: Incomplete | None = None,
        delta: Incomplete | None = None,
        see: bool = True,
    ) -> None: ...
    def configure(self, cnf: Incomplete = {}, **kw: Incomplete) -> None: ...
    def __setitem__(self, key: Incomplete, val: Incomplete) -> None: ...
    def rowconfigure(
        self, row_index: Incomplete, cnf: Incomplete = {}, **kw: Incomplete
    ) -> None: ...
    def columnconfigure(
        self, col_index: Incomplete, cnf: Incomplete = {}, **kw: Incomplete
    ) -> None: ...
    def itemconfigure(
        self,
        row_index: Incomplete,
        col_index: Incomplete,
        cnf: Incomplete | None = None,
        **kw: Incomplete,
    ) -> Incomplete: ...
    def insert(self, index: Incomplete, *rows: Incomplete) -> None: ...
    def get(
        self, first: Incomplete, last: Incomplete | None = None
    ) -> Incomplete: ...
    def bbox(self, row: Incomplete, col: Incomplete) -> Incomplete: ...
    def hide_column(self, col_index: Incomplete) -> None: ...
    def show_column(self, col_index: Incomplete) -> None: ...
    def bind_to_labels(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> Incomplete: ...
    def bind_to_listboxes(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> None: ...
    def bind_to_columns(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> Incomplete: ...
    def curselection(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def selection_includes(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def itemcget(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def size(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def index(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def nearest(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def activate(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def delete(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def scan_mark(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def scan_dragto(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def see(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def selection_anchor(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def selection_clear(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def selection_set(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def yview(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def yview_moveto(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def yview_scroll(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    itemconfig = itemconfigure
    rowconfig = rowconfigure
    columnconfig = columnconfigure
    select_anchor = selection_anchor
    select_clear = selection_clear
    select_includes = selection_includes
    select_set = selection_set

class Table:
    def __init__(
        self,
        master: Incomplete,
        column_names: Incomplete,
        rows: Incomplete | None = None,
        column_weights: Incomplete | None = None,
        scrollbar: bool = True,
        click_to_sort: bool = True,
        reprfunc: Incomplete | None = None,
        cnf: Incomplete = {},
        **kw: Incomplete,
    ) -> None: ...
    def pack(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def grid(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def focus(self) -> None: ...
    def bind(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> None: ...
    def rowconfigure(
        self, row_index: Incomplete, cnf: Incomplete = {}, **kw: Incomplete
    ) -> None: ...
    def columnconfigure(
        self, col_index: Incomplete, cnf: Incomplete = {}, **kw: Incomplete
    ) -> None: ...
    def itemconfigure(
        self,
        row_index: Incomplete,
        col_index: Incomplete,
        cnf: Incomplete | None = None,
        **kw: Incomplete,
    ) -> Incomplete: ...
    def bind_to_labels(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> Incomplete: ...
    def bind_to_listboxes(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> Incomplete: ...
    def bind_to_columns(
        self,
        sequence: Incomplete | None = None,
        func: Incomplete | None = None,
        add: Incomplete | None = None,
    ) -> Incomplete: ...
    rowconfig = rowconfigure
    columnconfig = columnconfigure
    itemconfig = itemconfigure
    def insert(self, row_index: Incomplete, rowvalue: Incomplete) -> None: ...
    def extend(self, rowvalues: Incomplete) -> None: ...
    def append(self, rowvalue: Incomplete) -> None: ...
    def clear(self) -> None: ...
    def __getitem__(self, index: Incomplete) -> Incomplete: ...
    def __setitem__(self, index: Incomplete, val: Incomplete) -> None: ...
    def __delitem__(self, row_index: Incomplete) -> None: ...
    def __len__(self) -> int: ...
    @property
    def column_names(self) -> Incomplete: ...
    def column_index(self, i: Incomplete) -> Incomplete: ...
    def hide_column(self, column_index: Incomplete) -> None: ...
    def show_column(self, column_index: Incomplete) -> None: ...
    def selected_row(self) -> Incomplete: ...
    def select(
        self,
        index: Incomplete | None = None,
        delta: Incomplete | None = None,
        see: bool = True,
    ) -> None: ...
    def sort_by(
        self, column_index: Incomplete, order: str = "toggle"
    ) -> None: ...

def demo() -> Incomplete: ...
