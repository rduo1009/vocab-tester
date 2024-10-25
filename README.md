# vocab-tester core (compatibility package experiment)
This was an experiment for creating a `_compat` package providing support for lower python versions (python3.9+ at the moment).
  
As this experiment progressed, I realised that the need to support lower python versions was not really needed – 
any user competent enough to build from source should also be competent enough to install the latest python version :slightly_smiling_face:.


## Setup
With poetry:
```shell
poetry install                                    # install dependencies
```
or just using pip:
```shell
python3 -m venv .venv                             # create virtual environment
source .venv/bin/activate                         # activate virtual environment
python3 -m pip install -r requirements.txt        # install regular dependencies
python3 -m pip install -r requirements-dev.txt    # install development dependencies (if required)
```
