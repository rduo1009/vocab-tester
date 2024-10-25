# vocab-tester core (coconut-lang experiment)
This was an experiment for using coconutlang to make the vocab-tester core compatible for python3.2+  
  
I decided to stop working on this as it became too difficult to keep the dependencies updated with such a low python version requirement.
To continue this, I would have had to:
* vendor most of the packages and transpile them using coconut
* find versions for the other packages where the versions would work with the project

which would likely be too much work.


## Setup
```shell
poetry install                       # install dependencies
coconut --keep-lines --fail-fast  .  # transpile python code to coconut
```
