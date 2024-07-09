import grammatica.endings

try:
    from icecream import install

    install()
    del install
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa: E731


verb = grammatica.endings.LearningVerb(
    pre="audio", inf="audire", per="audivi", ppp="auditus", meaning="hear"
)
ic(
    verb.get(
        person=2, number="singular", tense="present", voice="active", mood="infinitive"
    )
)

noun = grammatica.endings.Noun(nom="servus", gen="servi", gender="m", meaning="slave")
ic(noun.get(case="nominative", number="plural"))

adjective1 = grammatica.endings.Adjective212(
    mascnom="bonus", femnom="bona", neutnom="bonum", meaning="good"
)
ic(adjective1.get(gender="feminine", case="dative", number="singular"))

adjective2 = grammatica.endings.Adjective3(
    "ingens", "ingentis", termination=1, meaning="huge"
)

ic(adjective2.get(gender="masculine", case="genitive", number="plural"))

# path = Path(__file__).parent.joinpath("lists/test.txt")
# with open(path) as file:
#     grammatica.reader.read(file)
