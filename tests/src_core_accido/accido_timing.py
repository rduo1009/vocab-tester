import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import src
from codetiming import Timer

package_version = src.__version__

timing_file = "tests/src_core_accido/accido_timing_data.txt"


def log_timing_data(text):
    log_entry = f"version: {package_version}, {text}\n"

    with open(timing_file, mode="a") as file:
        file.write(log_entry)


@Timer(name="adjective", text="{name}: {seconds:.3f} s", logger=log_timing_data)
def time_adjective(run_times):
    from src.core.accido import endings

    for _ in range(run_times):
        endings.Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")


@Timer(name="noun", text="{name}: {seconds:.3f} s", logger=log_timing_data)
def time_noun(run_times):
    from src.core.accido import endings
    from src.core.accido.misc import Gender

    for _ in range(run_times):
        endings.Noun("ancilla", "ancillae", gender=Gender.FEMININE, meaning="slavegirl")


@Timer(name="verb", text="{name}: {seconds:.3f} s", logger=log_timing_data)
def time_verb(run_times):
    from src.core.accido import endings

    for _ in range(run_times):
        endings.Verb("celo", "celare", "celavi", "celatus", meaning="hide")


@Timer(name="pronoun", text="{name}: {seconds:.3f} s", logger=log_timing_data)
def time_pronoun(run_times):
    from src.core.accido import endings

    for _ in range(run_times):
        endings.Pronoun("hic", meaning="this")


if __name__ == "__main__":
    RUN_TIMES = 100_000

    time_adjective(RUN_TIMES)
    time_noun(RUN_TIMES)
    time_verb(RUN_TIMES)
    time_pronoun(RUN_TIMES)
