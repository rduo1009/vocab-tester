import grammatica.endings

try:
    from icecream import install  # type: ignore

    install()
    del install
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa: E731


verb = grammatica.endings.LearningVerb(
    present="audio",
    infinitive="audire",
    perfect="audivi",
    ppp="auditus",
    meaning="hear",
)
ic(
    verb.get(
        person=2, number="singular", tense="present", voice="active", mood="infinitive"
    )
)

noun = grammatica.endings.Noun(
    nominative="servus", genitive="servi", gender="m", meaning="slave"
)
ic(noun.get(case="nominative", number="plural"))


# path = Path(__file__).parent.joinpath("lists/test.txt")
# with open(path) as file:
#     grammatica.reader.read(file)
