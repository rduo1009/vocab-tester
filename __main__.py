import grammatica.endings

try:
    from icecream import install

    install()
    del install
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa: E731


verb = grammatica.endings.LearningVerb("audio", "audire", "audivi", "auditus", "hear")
ic(verb.get(2, "singular", "present", "active", "infinitive"))

noun = grammatica.endings.Noun("servus", "servi", "m", "slave")
ic(noun.get("nominative", "plural"))

adjective1 = grammatica.endings.Adjective212("bonus", "bona", "bonum", "good")
ic(adjective1.get("feminine", "dative", "singular"))

adjective2 = grammatica.endings.Adjective3(
    "ingens", "ingentis", termination=1, meaning="huge"
)

ic(adjective2.get("masculine", "genitive", "plural"))

# path = Path(__file__).parent.joinpath("lists/test.txt")
# with open(path) as file:
#     grammatica.reader.read(file)
