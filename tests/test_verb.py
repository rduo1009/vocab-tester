import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grammatica.endings import LearningVerb


def test_repr():
    word = LearningVerb("test1", "testare", "test3", "test4", "test5")
    assert word.__repr__() == "LearningVerb(test1, testare, test3, test4, test5)"


def test_eq():
    word1 = LearningVerb("test1", "testare", "test3", "test4", "test5")
    word2 = LearningVerb("test1", "testare", "test3", "test4", "test5")
    assert word1 == word2


def test_lt():
    word1 = LearningVerb("test1", "testare", "test3", "test4", "test5")
    word2 = LearningVerb("aaatest1", "testare", "test3", "test4", "test5")
    # word2 must be smaller than word1 as word1.first = "test1" and word2.first = "aaatest1"
    assert word1 > word2


def test_firstconjugation():
    word = LearningVerb(
        pre="celo", inf="celare", per="celavi", ppp="celatus", meaning="hide"
    )

    assert word.get(1, "singular", "present", "active", "indicative") == "celo"
    assert word.get(2, "singular", "present", "active", "indicative") == "celas"
    assert word.get(3, "singular", "present", "active", "indicative") == "celat"
    assert word.get(1, "plural", "present", "active", "indicative") == "celamus"
    assert word.get(2, "plural", "present", "active", "indicative") == "celatis"
    assert word.get(3, "plural", "present", "active", "indicative") == "celant"

    assert word.get(1, "singular", "imperfect", "active", "indicative") == "celabam"
    assert word.get(2, "singular", "imperfect", "active", "indicative") == "celabas"
    assert word.get(3, "singular", "imperfect", "active", "indicative") == "celabat"
    assert word.get(1, "plural", "imperfect", "active", "indicative") == "celabamus"
    assert word.get(2, "plural", "imperfect", "active", "indicative") == "celabatis"
    assert word.get(3, "plural", "imperfect", "active", "indicative") == "celabant"

    assert word.get(1, "singular", "perfect", "active", "indicative") == "celavi"
    assert word.get(2, "singular", "perfect", "active", "indicative") == "celavisti"
    assert word.get(3, "singular", "perfect", "active", "indicative") == "celavit"
    assert word.get(1, "plural", "perfect", "active", "indicative") == "celavimus"
    assert word.get(2, "plural", "perfect", "active", "indicative") == "celavistis"
    assert word.get(3, "plural", "perfect", "active", "indicative") == "celaverunt"

    assert word.get(1, "singular", "pluperfect", "active", "indicative") == "celaveram"
    assert word.get(2, "singular", "pluperfect", "active", "indicative") == "celaveras"
    assert word.get(3, "singular", "pluperfect", "active", "indicative") == "celaverat"
    assert word.get(1, "plural", "pluperfect", "active", "indicative") == "celaveramus"
    assert word.get(2, "plural", "pluperfect", "active", "indicative") == "celaveratis"
    assert word.get(3, "plural", "pluperfect", "active", "indicative") == "celaverant"

    assert word.get(None, None, "present", "active", "infinitive") == "celare"

    assert word.get(2, "singular", "present", "active", "imperative") == "cela"
    assert word.get(2, "plural", "present", "active", "imperative") == "celate"

    assert word.get(1, "singular", "imperfect", "active", "subjunctive") == "celarem"
    assert word.get(2, "singular", "imperfect", "active", "subjunctive") == "celares"
    assert word.get(3, "singular", "imperfect", "active", "subjunctive") == "celaret"
    assert word.get(1, "plural", "imperfect", "active", "subjunctive") == "celaremus"
    assert word.get(2, "plural", "imperfect", "active", "subjunctive") == "celaretis"
    assert word.get(3, "plural", "imperfect", "active", "subjunctive") == "celarent"

    assert (
        word.get(1, "singular", "pluperfect", "active", "subjunctive") == "celavissem"
    )
    assert (
        word.get(2, "singular", "pluperfect", "active", "subjunctive") == "celavisses"
    )
    assert (
        word.get(3, "singular", "pluperfect", "active", "subjunctive") == "celavisset"
    )
    assert (
        word.get(1, "plural", "pluperfect", "active", "subjunctive") == "celavissemus"
    )
    assert (
        word.get(2, "plural", "pluperfect", "active", "subjunctive") == "celavissetis"
    )
    assert word.get(3, "plural", "pluperfect", "active", "subjunctive") == "celavissent"


def test_secondconjugation():
    word = LearningVerb(
        pre="pareo", inf="parere", per="parui", ppp=None, meaning="hide"
    )

    assert word.get(1, "singular", "present", "active", "indicative") == "pareo"
    assert word.get(2, "singular", "present", "active", "indicative") == "pares"
    assert word.get(3, "singular", "present", "active", "indicative") == "paret"
    assert word.get(1, "plural", "present", "active", "indicative") == "paremus"
    assert word.get(2, "plural", "present", "active", "indicative") == "paretis"
    assert word.get(3, "plural", "present", "active", "indicative") == "parent"

    assert word.get(1, "singular", "imperfect", "active", "indicative") == "parebam"
    assert word.get(2, "singular", "imperfect", "active", "indicative") == "parebas"
    assert word.get(3, "singular", "imperfect", "active", "indicative") == "parebat"
    assert word.get(1, "plural", "imperfect", "active", "indicative") == "parebamus"
    assert word.get(2, "plural", "imperfect", "active", "indicative") == "parebatis"
    assert word.get(3, "plural", "imperfect", "active", "indicative") == "parebant"

    assert word.get(1, "singular", "perfect", "active", "indicative") == "parui"
    assert word.get(2, "singular", "perfect", "active", "indicative") == "paruisti"
    assert word.get(3, "singular", "perfect", "active", "indicative") == "paruit"
    assert word.get(1, "plural", "perfect", "active", "indicative") == "paruimus"
    assert word.get(2, "plural", "perfect", "active", "indicative") == "paruistis"
    assert word.get(3, "plural", "perfect", "active", "indicative") == "paruerunt"

    assert word.get(1, "singular", "pluperfect", "active", "indicative") == "parueram"
    assert word.get(2, "singular", "pluperfect", "active", "indicative") == "parueras"
    assert word.get(3, "singular", "pluperfect", "active", "indicative") == "paruerat"
    assert word.get(1, "plural", "pluperfect", "active", "indicative") == "parueramus"
    assert word.get(2, "plural", "pluperfect", "active", "indicative") == "parueratis"
    assert word.get(3, "plural", "pluperfect", "active", "indicative") == "paruerant"

    assert word.get(None, None, "present", "active", "infinitive") == "parere"

    assert word.get(2, "singular", "present", "active", "imperative") == "pare"
    assert word.get(2, "plural", "present", "active", "imperative") == "parete"

    assert word.get(1, "singular", "imperfect", "active", "subjunctive") == "parerem"
    assert word.get(2, "singular", "imperfect", "active", "subjunctive") == "pareres"
    assert word.get(3, "singular", "imperfect", "active", "subjunctive") == "pareret"
    assert word.get(1, "plural", "imperfect", "active", "subjunctive") == "pareremus"
    assert word.get(2, "plural", "imperfect", "active", "subjunctive") == "pareretis"
    assert word.get(3, "plural", "imperfect", "active", "subjunctive") == "parerent"

    assert word.get(1, "singular", "pluperfect", "active", "subjunctive") == "paruissem"
    assert word.get(2, "singular", "pluperfect", "active", "subjunctive") == "paruisses"
    assert word.get(3, "singular", "pluperfect", "active", "subjunctive") == "paruisset"
    assert word.get(1, "plural", "pluperfect", "active", "subjunctive") == "paruissemus"
    assert word.get(2, "plural", "pluperfect", "active", "subjunctive") == "paruissetis"
    assert word.get(3, "plural", "pluperfect", "active", "subjunctive") == "paruissent"


def test_thirdconjugation():
    word = LearningVerb(
        pre="desero", inf="deserere", per="deserui", ppp="desertus", meaning="desert"
    )
    assert word.get(1, "singular", "present", "active", "indicative") == "desero"
    assert word.get(2, "singular", "present", "active", "indicative") == "deseris"
    assert word.get(3, "singular", "present", "active", "indicative") == "deserit"
    assert word.get(1, "plural", "present", "active", "indicative") == "deserimus"
    assert word.get(2, "plural", "present", "active", "indicative") == "deseritis"
    assert word.get(3, "plural", "present", "active", "indicative") == "deserunt"

    assert word.get(1, "singular", "imperfect", "active", "indicative") == "deserebam"
    assert word.get(2, "singular", "imperfect", "active", "indicative") == "deserebas"
    assert word.get(3, "singular", "imperfect", "active", "indicative") == "deserebat"
    assert word.get(1, "plural", "imperfect", "active", "indicative") == "deserebamus"
    assert word.get(2, "plural", "imperfect", "active", "indicative") == "deserebatis"
    assert word.get(3, "plural", "imperfect", "active", "indicative") == "deserebant"

    assert word.get(1, "singular", "perfect", "active", "indicative") == "deserui"
    assert word.get(2, "singular", "perfect", "active", "indicative") == "deseruisti"
    assert word.get(3, "singular", "perfect", "active", "indicative") == "deseruit"
    assert word.get(1, "plural", "perfect", "active", "indicative") == "deseruimus"
    assert word.get(2, "plural", "perfect", "active", "indicative") == "deseruistis"
    assert word.get(3, "plural", "perfect", "active", "indicative") == "deseruerunt"

    assert word.get(1, "singular", "pluperfect", "active", "indicative") == "deserueram"
    assert word.get(2, "singular", "pluperfect", "active", "indicative") == "deserueras"
    assert word.get(3, "singular", "pluperfect", "active", "indicative") == "deseruerat"
    assert word.get(1, "plural", "pluperfect", "active", "indicative") == "deserueramus"
    assert word.get(2, "plural", "pluperfect", "active", "indicative") == "deserueratis"
    assert word.get(3, "plural", "pluperfect", "active", "indicative") == "deseruerant"

    assert word.get(None, None, "present", "active", "infinitive") == "deserere"

    assert word.get(2, "singular", "present", "active", "imperative") == "desere"
    assert word.get(2, "plural", "present", "active", "imperative") == "deserite"

    assert word.get(1, "singular", "imperfect", "active", "subjunctive") == "desererem"
    assert word.get(2, "singular", "imperfect", "active", "subjunctive") == "desereres"
    assert word.get(3, "singular", "imperfect", "active", "subjunctive") == "desereret"
    assert word.get(1, "plural", "imperfect", "active", "subjunctive") == "desereremus"
    assert word.get(2, "plural", "imperfect", "active", "subjunctive") == "desereretis"
    assert word.get(3, "plural", "imperfect", "active", "subjunctive") == "desererent"

    assert (
        word.get(1, "singular", "pluperfect", "active", "subjunctive") == "deseruissem"
    )
    assert (
        word.get(2, "singular", "pluperfect", "active", "subjunctive") == "deseruisses"
    )
    assert (
        word.get(3, "singular", "pluperfect", "active", "subjunctive") == "deseruisset"
    )
    assert (
        word.get(1, "plural", "pluperfect", "active", "subjunctive") == "deseruissemus"
    )
    assert (
        word.get(2, "plural", "pluperfect", "active", "subjunctive") == "deseruissetis"
    )
    assert (
        word.get(3, "plural", "pluperfect", "active", "subjunctive") == "deseruissent"
    )


def test_thirdioconjugation():
    word = LearningVerb(
        pre="patefacio",
        inf="patefacere",
        per="patefeci",
        ppp="patefactus",
        meaning="reveal",
    )
    assert word.get(1, "singular", "present", "active", "indicative") == "patefacio"
    assert word.get(2, "singular", "present", "active", "indicative") == "patefacis"
    assert word.get(3, "singular", "present", "active", "indicative") == "patefacit"
    assert word.get(1, "plural", "present", "active", "indicative") == "patefacimus"
    assert word.get(2, "plural", "present", "active", "indicative") == "patefacitis"
    assert word.get(3, "plural", "present", "active", "indicative") == "patefaciunt"

    assert (
        word.get(1, "singular", "imperfect", "active", "indicative") == "patefaciebam"
    )
    assert (
        word.get(2, "singular", "imperfect", "active", "indicative") == "patefaciebas"
    )
    assert (
        word.get(3, "singular", "imperfect", "active", "indicative") == "patefaciebat"
    )
    assert (
        word.get(1, "plural", "imperfect", "active", "indicative") == "patefaciebamus"
    )
    assert (
        word.get(2, "plural", "imperfect", "active", "indicative") == "patefaciebatis"
    )
    assert word.get(3, "plural", "imperfect", "active", "indicative") == "patefaciebant"

    assert word.get(1, "singular", "perfect", "active", "indicative") == "patefeci"
    assert word.get(2, "singular", "perfect", "active", "indicative") == "patefecisti"
    assert word.get(3, "singular", "perfect", "active", "indicative") == "patefecit"
    assert word.get(1, "plural", "perfect", "active", "indicative") == "patefecimus"
    assert word.get(2, "plural", "perfect", "active", "indicative") == "patefecistis"
    assert word.get(3, "plural", "perfect", "active", "indicative") == "patefecerunt"

    assert (
        word.get(1, "singular", "pluperfect", "active", "indicative") == "patefeceram"
    )
    assert (
        word.get(2, "singular", "pluperfect", "active", "indicative") == "patefeceras"
    )
    assert (
        word.get(3, "singular", "pluperfect", "active", "indicative") == "patefecerat"
    )
    assert (
        word.get(1, "plural", "pluperfect", "active", "indicative") == "patefeceramus"
    )
    assert (
        word.get(2, "plural", "pluperfect", "active", "indicative") == "patefeceratis"
    )
    assert word.get(3, "plural", "pluperfect", "active", "indicative") == "patefecerant"

    assert word.get(None, None, "present", "active", "infinitive") == "patefacere"

    assert word.get(2, "singular", "present", "active", "imperative") == "pateface"
    assert word.get(2, "plural", "present", "active", "imperative") == "patefacite"

    assert (
        word.get(1, "singular", "imperfect", "active", "subjunctive") == "patefacerem"
    )
    assert (
        word.get(2, "singular", "imperfect", "active", "subjunctive") == "patefaceres"
    )
    assert (
        word.get(3, "singular", "imperfect", "active", "subjunctive") == "patefaceret"
    )
    assert (
        word.get(1, "plural", "imperfect", "active", "subjunctive") == "patefaceremus"
    )
    assert (
        word.get(2, "plural", "imperfect", "active", "subjunctive") == "patefaceretis"
    )
    assert word.get(3, "plural", "imperfect", "active", "subjunctive") == "patefacerent"

    assert (
        word.get(1, "singular", "pluperfect", "active", "subjunctive") == "patefecissem"
    )
    assert (
        word.get(2, "singular", "pluperfect", "active", "subjunctive") == "patefecisses"
    )
    assert (
        word.get(3, "singular", "pluperfect", "active", "subjunctive") == "patefecisset"
    )
    assert (
        word.get(1, "plural", "pluperfect", "active", "subjunctive") == "patefecissemus"
    )
    assert (
        word.get(2, "plural", "pluperfect", "active", "subjunctive") == "patefecissetis"
    )
    assert (
        word.get(3, "plural", "pluperfect", "active", "subjunctive") == "patefecissent"
    )


def test_fourthconjugation():
    word = LearningVerb(
        pre="aperio", inf="aperire", per="aperui", ppp="apertus", meaning="open"
    )

    assert word.get(1, "singular", "present", "active", "indicative") == "aperio"
    assert word.get(2, "singular", "present", "active", "indicative") == "aperis"
    assert word.get(3, "singular", "present", "active", "indicative") == "aperit"
    assert word.get(1, "plural", "present", "active", "indicative") == "aperimus"
    assert word.get(2, "plural", "present", "active", "indicative") == "aperitis"
    assert word.get(3, "plural", "present", "active", "indicative") == "aperiunt"

    assert word.get(1, "singular", "imperfect", "active", "indicative") == "aperiebam"
    assert word.get(2, "singular", "imperfect", "active", "indicative") == "aperiebas"
    assert word.get(3, "singular", "imperfect", "active", "indicative") == "aperiebat"
    assert word.get(1, "plural", "imperfect", "active", "indicative") == "aperiebamus"
    assert word.get(2, "plural", "imperfect", "active", "indicative") == "aperiebatis"
    assert word.get(3, "plural", "imperfect", "active", "indicative") == "aperiebant"

    assert word.get(1, "singular", "perfect", "active", "indicative") == "aperui"
    assert word.get(2, "singular", "perfect", "active", "indicative") == "aperuisti"
    assert word.get(3, "singular", "perfect", "active", "indicative") == "aperuit"
    assert word.get(1, "plural", "perfect", "active", "indicative") == "aperuimus"
    assert word.get(2, "plural", "perfect", "active", "indicative") == "aperuistis"
    assert word.get(3, "plural", "perfect", "active", "indicative") == "aperuerunt"

    assert word.get(1, "singular", "pluperfect", "active", "indicative") == "aperueram"
    assert word.get(2, "singular", "pluperfect", "active", "indicative") == "aperueras"
    assert word.get(3, "singular", "pluperfect", "active", "indicative") == "aperuerat"
    assert word.get(1, "plural", "pluperfect", "active", "indicative") == "aperueramus"
    assert word.get(2, "plural", "pluperfect", "active", "indicative") == "aperueratis"
    assert word.get(3, "plural", "pluperfect", "active", "indicative") == "aperuerant"

    assert word.get(None, None, "present", "active", "infinitive") == "aperire"

    assert word.get(2, "singular", "present", "active", "imperative") == "aperi"
    assert word.get(2, "plural", "present", "active", "imperative") == "aperite"

    assert word.get(1, "singular", "imperfect", "active", "subjunctive") == "aperirem"
    assert word.get(2, "singular", "imperfect", "active", "subjunctive") == "aperires"
    assert word.get(3, "singular", "imperfect", "active", "subjunctive") == "aperiret"
    assert word.get(1, "plural", "imperfect", "active", "subjunctive") == "aperiremus"
    assert word.get(2, "plural", "imperfect", "active", "subjunctive") == "aperiretis"
    assert word.get(3, "plural", "imperfect", "active", "subjunctive") == "aperirent"

    assert (
        word.get(1, "singular", "pluperfect", "active", "subjunctive") == "aperuissem"
    )
    assert (
        word.get(2, "singular", "pluperfect", "active", "subjunctive") == "aperuisses"
    )
    assert (
        word.get(3, "singular", "pluperfect", "active", "subjunctive") == "aperuisset"
    )
    assert (
        word.get(1, "plural", "pluperfect", "active", "subjunctive") == "aperuissemus"
    )
    assert (
        word.get(2, "plural", "pluperfect", "active", "subjunctive") == "aperuissetis"
    )
    assert word.get(3, "plural", "pluperfect", "active", "subjunctive") == "aperuissent"
