# mypy: ignore-errors

import importlib
import os
import sys
import warnings

warnings.filterwarnings("ignore")

RUN_TIMES = 100_000

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    test_dir = os.path.dirname(os.path.abspath(__file__))

    for dirpath, _, filenames in os.walk(test_dir):
        for filename in filenames:
            if filename.startswith("timing_") and filename.endswith(".py"):
                if dirpath not in sys.path:
                    sys.path.append(dirpath)

                module_name = filename[:-3]
                module = importlib.import_module(module_name)

                for attr_name in dir(module):
                    if attr_name.startswith("time_"):
                        timing_func = getattr(module, attr_name)

                        if callable(timing_func):
                            # print(f"Running {timing_func.__name__}...")
                            timing_func(RUN_TIMES)
