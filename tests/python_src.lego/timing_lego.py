import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import python_src
from codetiming import Timer
from python_src.lego.misc import VocabList

l: VocabList

package_version = python_src.__version__

timing_file = "tests/python_src.lego/lego_timing_data.txt"


def log_timing_data(text):
    log_entry = f"version: {package_version}, {text}\n"

    with open(timing_file, mode="a") as file:
        file.write(log_entry)


@Timer(name="reader", text="{name}: {seconds:.3f} s", logger=log_timing_data)
def time_reader(run_times):
    global l

    from pathlib import Path

    from python_src.lego.reader import read_vocab_file

    for _ in range(run_times):
        l = read_vocab_file(Path("tests/python_src.lego/test_vocab_files/regular_list.txt"))


@Timer(name="saver", text="{name}: {seconds:.3f} s", logger=log_timing_data)
def time_saver(run_times):
    global l

    from pathlib import Path

    from python_src.lego.saver import save_vocab_dump

    for _ in range(run_times):
        s = save_vocab_dump(Path("tests/python_src.lego/test_vocab_files/testdump/regular_list.testdump"), l)


if __name__ == "__main__":
    RUN_TIMES = 100_000

    time_reader(RUN_TIMES)
    time_saver(RUN_TIMES)
