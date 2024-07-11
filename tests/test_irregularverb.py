import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grammatica.endings import LearningVerb


def test_irregularverb_eo():
    word = LearningVerb(
        pre="abeo", inf="abire", per="abii", ppp="abitum", meaning="depart"
    )

    assert word.get(1, "singular", "present", "active", "indicative") == "abeo"
    assert word.get(2, "singular", "present", "active", "indicative") == "abis"
    assert word.get(3, "singular", "present", "active", "indicative") == "abit"
    assert word.get(1, "plural", "present", "active", "indicative") == "abimus"
    assert word.get(2, "plural", "present", "active", "indicative") == "abitis"
    assert word.get(3, "plural", "present", "active", "indicative") == "abeunt"

    assert word.get(1, "singular", "imperfect", "active", "indicative") == "abibam"

    assert word.get(2, "singular", "imperfect", "active", "indicative") == "abibas"
    assert word.get(3, "singular", "imperfect", "active", "indicative") == "abibat"
    assert word.get(1, "plural", "imperfect", "active", "indicative") == "abibamus"
    assert word.get(2, "plural", "imperfect", "active", "indicative") == "abibatis"
    assert word.get(3, "plural", "imperfect", "active", "indicative") == "abibant"

    assert word.get(1, "singular", "perfect", "active", "indicative") == "abii"
    assert word.get(2, "singular", "perfect", "active", "indicative") == "abisti"
    assert word.get(3, "singular", "perfect", "active", "indicative") == "abiit"
    assert word.get(1, "plural", "perfect", "active", "indicative") == "abiimus"
    assert word.get(2, "plural", "perfect", "active", "indicative") == "abistis"
    assert word.get(3, "plural", "perfect", "active", "indicative") == "abierunt"

    assert word.get(1, "singular", "pluperfect", "active", "indicative") == "abieram"
    assert word.get(2, "singular", "pluperfect", "active", "indicative") == "abieras"
    assert word.get(3, "singular", "pluperfect", "active", "indicative") == "abierat"
    assert word.get(1, "plural", "pluperfect", "active", "indicative") == "abieramus"
    assert word.get(2, "plural", "pluperfect", "active", "indicative") == "abieratis"
    assert word.get(3, "plural", "pluperfect", "active", "indicative") == "abierant"

    assert word.get(None, None, "present", "active", "infinitive") == "abire"

    assert word.get(2, "singular", "present", "active", "imperative") == "abi"
    assert word.get(2, "plural", "present", "active", "imperative") == "abite"

    assert word.get(1, "singular", "imperfect", "active", "subjunctive") == "abirem"
    assert word.get(2, "singular", "imperfect", "active", "subjunctive") == "abires"
    assert word.get(3, "singular", "imperfect", "active", "subjunctive") == "abiret"
    assert word.get(1, "plural", "imperfect", "active", "subjunctive") == "abiremus"
    assert word.get(2, "plural", "imperfect", "active", "subjunctive") == "abiretis"
    assert word.get(3, "plural", "imperfect", "active", "subjunctive") == "abirent"

    assert word.get(1, "singular", "pluperfect", "active", "subjunctive") == "abissem"
    assert word.get(2, "singular", "pluperfect", "active", "subjunctive") == "abisses"
    assert word.get(3, "singular", "pluperfect", "active", "subjunctive") == "abisset"
    assert word.get(1, "plural", "pluperfect", "active", "subjunctive") == "abissemus"
    assert word.get(2, "plural", "pluperfect", "active", "subjunctive") == "abissetis"
    assert word.get(3, "plural", "pluperfect", "active", "subjunctive") == "abissent"
