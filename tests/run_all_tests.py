import os
import sys
import importlib

if __name__ == "__main__":
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    )

    test_dir = os.path.dirname(os.path.abspath(__file__))

    for dirpath, _, filenames in os.walk(test_dir):
        for filename in filenames:
            if filename.startswith("test_") and filename.endswith(".py"):
                if dirpath not in sys.path:
                    sys.path.append(dirpath)
                module_name = filename[:-3]
                module = importlib.import_module(module_name)
                for attr_name in dir(module):
                    if attr_name.startswith("test_"):
                        test_func = getattr(module, attr_name)
                        if callable(test_func):
                            test_func()
