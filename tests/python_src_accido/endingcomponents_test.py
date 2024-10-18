import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from python_src.accido.misc import Case, Degree, EndingComponents, Gender, Number


class TestEndingComponentsDunder:
    def test_eq(self):
        a = EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER)
        b = EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER)
        assert a == b

    def test_noeq(self):
        a = EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER)
        b = EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER, degree=Degree.POSITIVE)
        assert a != b

    def test_hash(self):
        a = EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER)
        b = EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER)
        assert hash(a) == hash(b)
