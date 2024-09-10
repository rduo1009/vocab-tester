# mypy: ignore-errors

import importlib
import inspect
import os
import sys
import warnings

warnings.filterwarnings("ignore")


def run_tests_in_class(cls):
    instance = cls()

    for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
        if name.startswith("test_"):
            func(instance)
            # print(f"Running {cls.__name__}.{test_func.__name__}...")


if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    test_dir = os.path.dirname(os.path.abspath(__file__))

    for dirpath, _, filenames in os.walk(test_dir):
        for filename in filenames:
            if filename.endswith("_test.py"):
                if dirpath not in sys.path:
                    sys.path.append(dirpath)

                module_name = filename[:-3]
                module = importlib.import_module(module_name)

                for attr_name in dir(module):
                    if attr_name.startswith("test_"):
                        test_func = getattr(module, attr_name)

                        if callable(test_func):
                            # print(f"Running {test_func.__name__}...")
                            test_func()
                    elif attr_name.startswith("Test"):
                        cls = getattr(module, attr_name)
                        run_tests_in_class(cls)
