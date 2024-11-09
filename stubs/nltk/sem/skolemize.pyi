from _typeshed import Incomplete

from nltk.sem.logic import (
    AllExpression as AllExpression,
)
from nltk.sem.logic import (
    AndExpression as AndExpression,
)
from nltk.sem.logic import (
    ApplicationExpression as ApplicationExpression,
)
from nltk.sem.logic import (
    EqualityExpression as EqualityExpression,
)
from nltk.sem.logic import (
    ExistsExpression as ExistsExpression,
)
from nltk.sem.logic import (
    IffExpression as IffExpression,
)
from nltk.sem.logic import (
    ImpExpression as ImpExpression,
)
from nltk.sem.logic import (
    NegatedExpression as NegatedExpression,
)
from nltk.sem.logic import (
    OrExpression as OrExpression,
)
from nltk.sem.logic import (
    VariableExpression as VariableExpression,
)
from nltk.sem.logic import (
    skolem_function as skolem_function,
)
from nltk.sem.logic import (
    unique_variable as unique_variable,
)

def skolemize(
    expression: Incomplete,
    univ_scope: Incomplete | None = None,
    used_variables: Incomplete | None = None,
) -> Incomplete: ...
def to_cnf(first: Incomplete, second: Incomplete) -> Incomplete: ...
