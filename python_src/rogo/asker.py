#!/usr/bin/env python3

"""Contains functions that generate questions and check answers."""

from __future__ import annotations

import random
from copy import deepcopy
from typing import TYPE_CHECKING, overload

from .. import accido, lego, transfero
from ..accido.misc import Case, Gender, Mood, Number
from ..utils import set_choice
from .exceptions import InvalidSettingsError
from .question_classes import (
    MultipleChoiceEngToLatQuestion,
    MultipleChoiceLattoEngQuestion,
    ParseWordCompToLatQuestion,
    ParseWordLatToCompQuestion,
    PrincipalPartsQuestion,
    QuestionClasses,
    TypeInEngToLatQuestion,
    TypeInLatToEngQuestion,
)
from .rules import filter_endings, filter_questions, filter_words

if TYPE_CHECKING:
    from collections.abc import Iterable

    from ..accido.type_aliases import Ending, Endings, Meaning
    from .question_classes import Question
    from .type_aliases import Settings, Vocab


def _pick_ending(
    endings: Endings,
) -> tuple[str, Ending]:
    return random.choice(list(endings.items()))


def ask_question_without_sr(
    vocab_list: lego.misc.VocabList, amount: int, settings: Settings
) -> Iterable[Question]:
    """Ask a question about Latin vocabulary.

    Parameters
    ----------
    vocab_list : lego.misc.VocabList
        The vocabulary list to use.
    amount : int
        The number of questions to ask.
    settings : Settings
        The settings to use.

    Yields
    ------
    Question
        The question to ask.

    Raises
    ------
    InvalidSettingsError
        If the settings are invalid.
    """
    vocab: Vocab = filter_words(vocab_list, settings)
    filtered_questions: set[QuestionClasses] = filter_questions(settings)

    if len(vocab_list.vocab) < settings["number-multiplechoice-options"]:
        filtered_questions.discard(QuestionClasses.MULTIPLECHOICE_ENGTOLAT)
        filtered_questions.discard(QuestionClasses.MULTIPLECHOICE_LATTOENG)

    if not filtered_questions:
        raise InvalidSettingsError("No question type has been enabled.")

    for _ in range(amount):
        chosen_word: accido.endings._Word = random.choice(vocab)
        filtered_endings: Endings = filter_endings(
            chosen_word.endings, settings
        )
        if not filtered_endings:
            continue

        question_type: QuestionClasses = set_choice(filtered_questions)

        # TODO: if ever using mypyc, make a new variable for every type
        # for now, any type to allow variable to be reused
        output: Question | None
        match question_type:
            case QuestionClasses.TYPEIN_ENGTOLAT:
                if output := _generate_typein_engtolat(
                    chosen_word, filtered_endings
                ):
                    yield output
                else:
                    continue

            case QuestionClasses.TYPEIN_LATTOENG:
                if output := _generate_typein_lattoeng(
                    chosen_word, filtered_endings
                ):
                    yield output
                else:
                    continue

            case QuestionClasses.PARSEWORD_LATTOCOMP:
                if output := _generate_parse(chosen_word, filtered_endings):
                    yield output
                else:
                    continue

            case QuestionClasses.PARSEWORD_COMPTOLAT:
                if output := _generate_inflect(chosen_word, filtered_endings):
                    yield output
                else:
                    continue

            case QuestionClasses.PRINCIPAL_PARTS:
                if output := _generate_principal_parts_question(chosen_word):
                    yield output
                else:
                    continue

            case QuestionClasses.MULTIPLECHOICE_ENGTOLAT:
                yield _generate_multiplechoice_engtolat(
                    vocab,
                    chosen_word,
                    settings["number-multiplechoice-options"],
                )

            case QuestionClasses.MULTIPLECHOICE_LATTOENG:
                yield _generate_multiplechoice_lattoeng(
                    vocab,
                    chosen_word,
                    settings["number-multiplechoice-options"],
                )


def _pick_ending_from_multipleendings(ending: Ending) -> str:
    if type(ending) is accido.misc.MultipleEndings:
        return random.choice(ending.get_all())

    assert type(ending) is str
    return ending


def _generate_typein_engtolat(  # noqa: PLR0914, PLR0915
    chosen_word: accido.endings._Word, filtered_endings: Endings
) -> TypeInEngToLatQuestion | None:
    ending_components_key: str
    chosen_ending: Ending
    ending_components_key, chosen_ending = _pick_ending(filtered_endings)

    chosen_ending = _pick_ending_from_multipleendings(chosen_ending)

    # HACK: Uses a private method but there's no alternative
    ending_components: accido.misc.EndingComponents = (
        chosen_word._create_components(ending_components_key)  # noqa: SLF001
    )

    verb_subjunctive: bool = (  # not supported with this question
        type(chosen_word) is accido.endings.Verb
        and ending_components.mood == Mood.SUBJUNCTIVE
    )

    noun_accusative_vocative: bool = (  # considered same as nominative
        type(chosen_word) is accido.endings.Noun
        and ending_components.case in {Case.ACCUSATIVE, Case.VOCATIVE}
    )

    adjective_flag: bool = hasattr(ending_components, "case")
    adjective_nominative: bool = (  # adjectives are all same
        type(chosen_word) is accido.endings.Adjective
        and adjective_flag
        and ending_components.case != Case.NOMINATIVE
        and ending_components.number != Number.SINGULAR
    )

    participle_nominative: bool = (
        type(chosen_word) is accido.endings.Verb
        and ending_components.subtype == "participle"
        and ending_components.case != Case.NOMINATIVE
        and ending_components.number != Number.SINGULAR
        and ending_components.gender == Gender.MASCULINE
    )

    verb_second_plural: bool = (  # plural 2nd person is same as singular
        type(chosen_word) is accido.endings.Verb
        and ending_components.subtype not in {"infinitive", "participle"}
        and ending_components.number == Number.PLURAL
        and ending_components.person == 2
    )

    pronoun_flag: bool = type(chosen_word) is accido.endings.Pronoun or (
        type(chosen_word) is accido.endings.Noun
        and ending_components.subtype == "pronoun"
    )
    pronoun_not_masculine: bool = (
        pronoun_flag and ending_components.gender != Gender.MASCULINE
    )

    if (
        verb_subjunctive  # noqa: PLR0916
        or noun_accusative_vocative
        or adjective_nominative
        or participle_nominative
        or verb_second_plural
        or pronoun_not_masculine
    ):
        return None

    # Get the best meaning if it is a MultipleMeanings, or
    # just the meaning if it is a string
    raw_meaning: str = str(chosen_word.meaning)
    inflected_meaning: str = set_choice(
        transfero.words.find_inflection(
            word=raw_meaning, components=ending_components
        )
    )

    answers: set[str] = {chosen_ending}
    if (  # nominative, accusative and vocative considered same
        type(chosen_word) is accido.endings.Noun
        and ending_components.case == Case.NOMINATIVE
    ):
        answers = {chosen_ending}
        endings_to_add: tuple[Ending | None, ...] = (
            chosen_word.get(
                case=Case.ACCUSATIVE, number=ending_components.number
            ),
            chosen_word.get(
                case=Case.VOCATIVE, number=ending_components.number
            ),
        )
        for ending in endings_to_add:
            if type(ending) is str:
                answers.add(ending)
            elif type(ending) is accido.misc.MultipleEndings:
                answers.update(ending.get_all())

    elif type(chosen_word) is accido.endings.Adjective and adjective_flag:
        answers = {
            item
            for key, value in chosen_word.endings.items()
            if key.startswith("A")
            and key[1:4] == ending_components.degree.shorthand
            # HACK: A little weird but it works (avoids unpacking)
            for item in (
                value.get_all()
                if isinstance(value, accido.misc.MultipleEndings)
                else [value]
            )
        }

        if ending_components.number == Number.PLURAL:
            chosen_ending = str(  # str to get the main ending
                chosen_word.get(
                    case=Case.NOMINATIVE,
                    number=Number.SINGULAR,
                    gender=Gender.MASCULINE,
                    degree=ending_components.degree,
                )
            )

    elif (
        type(chosen_word) is accido.endings.Verb
        and ending_components.subtype == "participle"
    ):
        answers = {
            item
            for key, value in chosen_word.endings.items()
            if key[7:10] == Mood.PARTICIPLE.shorthand
            for item in (
                value.get_all()
                if isinstance(value, accido.misc.MultipleEndings)
                else [value]
            )
        }

        if ending_components.number == Number.PLURAL:
            chosen_ending = str(  # str to get the main ending
                chosen_word.get(
                    tense=ending_components.tense,
                    voice=ending_components.voice,
                    mood=Mood.PARTICIPLE,
                    number=Number.SINGULAR,
                    participle_case=Case.NOMINATIVE,
                    participle_gender=Gender.MASCULINE,
                )
            )

    elif (
        type(chosen_word) is accido.endings.Verb
        and ending_components.subtype not in {"infinitive", "participle"}
        and ending_components.person == 2
    ):
        # HACK: messy but works
        if second_person_plural := chosen_word.get(
            tense=ending_components.tense,
            voice=ending_components.voice,
            mood=ending_components.mood,
            number=Number.PLURAL,
            person=2,
        ):
            temp_second_person_plural: tuple[str, ...]
            if type(second_person_plural) is accido.misc.MultipleEndings:
                temp_second_person_plural = tuple(
                    second_person_plural.get_all()
                )
            else:
                assert type(second_person_plural) is str
                temp_second_person_plural = (second_person_plural,)

            answers = {
                chosen_ending,  # second person singular
                *temp_second_person_plural,
            }
        else:
            answers = {chosen_ending}

    elif pronoun_flag:

        @overload
        def _convert_to_tuple(ending: Ending) -> tuple[str, ...]: ...
        @overload
        def _convert_to_tuple(ending: None) -> tuple[None]: ...

        def _convert_to_tuple(
            ending: Ending | None,
        ) -> tuple[str, ...] | tuple[None]:
            if ending is None:
                return ()

            if type(ending) is accido.misc.MultipleEndings:
                return tuple(ending.get_all())

            assert type(ending) is str
            return (ending,)

        answers = {
            *_convert_to_tuple(
                chosen_word.get(
                    case=ending_components.case,
                    number=ending_components.number,
                    gender=Gender.MASCULINE,
                )
            ),
            *_convert_to_tuple(
                chosen_word.get(
                    case=ending_components.case,
                    number=ending_components.number,
                    gender=Gender.FEMININE,
                )
            ),
            *_convert_to_tuple(
                chosen_word.get(
                    case=ending_components.case,
                    number=ending_components.number,
                    gender=Gender.NEUTER,
                )
            ),
        }

    return TypeInEngToLatQuestion(
        prompt=inflected_meaning, main_answer=chosen_ending, answers=answers
    )


def _generate_typein_lattoeng(
    chosen_word: accido.endings._Word, filtered_endings: Endings
) -> TypeInLatToEngQuestion | None:
    chosen_ending: Ending
    _, chosen_ending = _pick_ending(filtered_endings)

    chosen_ending = _pick_ending_from_multipleendings(chosen_ending)

    inflected_meanings: set[str] = set()

    # to allow for multiple endingcomponents for one ending
    # e.g. 'puellae' could be nominative plural or genitive singular
    all_ending_components: list[accido.misc.EndingComponents] = (
        chosen_word.find(chosen_ending)
    )
    # TODO: create function get_main_inflection for each word type
    # then use it here
    possible_main_answers: set[str] = set()

    def _generate_inflections(
        ending_components: accido.misc.EndingComponents,
    ) -> None:
        verb_subjunctive: bool = (  # not supported with this question
            type(chosen_word) is accido.endings.Verb
            and ending_components.mood == Mood.SUBJUNCTIVE
        )
        # if the mood was subjunctive, nothing happens
        if verb_subjunctive:
            return

        raw_meanings: Meaning = chosen_word.meaning
        main_meaning: str
        meanings: set[str]
        if type(raw_meanings) is accido.misc.MultipleMeanings:
            # using the fact that __str__ returns the main meaning
            main_meaning = str(raw_meanings)
            meanings = set(raw_meanings.meanings)
        else:
            assert type(raw_meanings) is str
            meanings = {raw_meanings}
            main_meaning = raw_meanings

        meaning: str
        for meaning in meanings:
            inflected_meanings.update(
                transfero.words.find_inflection(
                    word=meaning, components=ending_components
                )
            )

        possible_main_answers.add(
            set_choice(
                transfero.words.find_inflection(
                    word=main_meaning, components=ending_components
                )
            )
        )

    for ending_components in all_ending_components:
        _generate_inflections(ending_components=ending_components)

    if not possible_main_answers:
        return None
    main_answer: str = random.choice(tuple(possible_main_answers))

    return TypeInLatToEngQuestion(
        prompt=chosen_ending,
        main_answer=main_answer,
        answers=inflected_meanings,
    )


def _generate_parse(
    chosen_word: accido.endings._Word, filtered_endings: Endings
) -> ParseWordLatToCompQuestion | None:
    if type(chosen_word) is accido.endings.RegularWord:
        return None

    ending_components_key: str
    chosen_ending: Ending
    ending_components_key, chosen_ending = _pick_ending(filtered_endings)

    main_ending_components: accido.misc.EndingComponents = (
        chosen_word._create_components(ending_components_key)  # noqa: SLF001
    )

    chosen_ending = _pick_ending_from_multipleendings(chosen_ending)

    all_ending_components: set[accido.misc.EndingComponents] = set(
        chosen_word.find(chosen_ending)
    )
    assert main_ending_components in all_ending_components

    return ParseWordLatToCompQuestion(
        prompt=chosen_ending,
        main_answer=main_ending_components,
        answers=all_ending_components,
        dictionary_entry=str(chosen_word),  # __str__ returns dictionary entry
    )


def _generate_inflect(
    chosen_word: accido.endings._Word, filtered_endings: Endings
) -> ParseWordCompToLatQuestion | None:
    if type(chosen_word) is accido.endings.RegularWord:
        return None

    ending_components_key: str
    chosen_ending: Ending
    ending_components_key, chosen_ending = _pick_ending(filtered_endings)

    ending_components: accido.misc.EndingComponents = (
        chosen_word._create_components(ending_components_key)  # noqa: SLF001
    )

    main_answer: str
    answers: set[str]
    if type(chosen_ending) is accido.misc.MultipleEndings:
        if hasattr(chosen_ending, "regular"):
            main_answer = chosen_ending.regular
        else:
            main_answer = random.choice(chosen_ending.get_all())
        answers = set(chosen_ending.get_all())
    else:
        assert type(chosen_ending) is str
        main_answer = chosen_ending
        answers = {chosen_ending}

    return ParseWordCompToLatQuestion(
        prompt=str(chosen_word),  # __str__ returns dictionary entry
        components=ending_components,
        main_answer=main_answer,
        answers=answers,
    )


def _generate_principal_parts_question(
    chosen_word: accido.endings._Word,
) -> PrincipalPartsQuestion | None:
    if type(chosen_word) is accido.endings.RegularWord:
        return None

    principal_parts: tuple[str, ...]
    if type(chosen_word) is accido.endings.Verb:
        if chosen_word.ppp:
            principal_parts = (
                chosen_word.present,
                chosen_word.infinitive,
                chosen_word.perfect,
                chosen_word.ppp,
            )
        else:
            principal_parts = (
                chosen_word.present,
                chosen_word.infinitive,
                chosen_word.perfect,
            )

    elif type(chosen_word) is accido.endings.Noun:
        if chosen_word.genitive:
            principal_parts = (chosen_word.nominative, chosen_word.genitive)
        else:  # irregular noun
            return None

    elif type(chosen_word) is accido.endings.Adjective:
        match chosen_word.declension:
            case "212":
                principal_parts = (
                    chosen_word.mascnom,
                    chosen_word.femnom,
                    chosen_word.neutnom,
                )
            case "3":
                match chosen_word.termination:
                    case 1:
                        principal_parts = (
                            chosen_word.mascnom,
                            chosen_word.mascgen,
                        )
                    case 2:
                        principal_parts = (
                            chosen_word.mascnom,
                            chosen_word.neutnom,
                        )
                    case 3:
                        principal_parts = (
                            chosen_word.mascnom,
                            chosen_word.femnom,
                            chosen_word.neutnom,
                        )

    elif type(chosen_word) is accido.endings.Pronoun:
        principal_parts = (
            chosen_word.mascnom,
            chosen_word.femnom,
            chosen_word.neutnom,
        )

    return PrincipalPartsQuestion(
        prompt=principal_parts[0], principal_parts=principal_parts
    )


def _generate_multiplechoice_engtolat(
    vocab_list: Vocab,
    chosen_word: accido.endings._Word,
    number_multiplechoice_options: int,
) -> MultipleChoiceEngToLatQuestion:
    vocab_list = deepcopy(vocab_list)
    vocab_list.remove(chosen_word)

    meaning: Meaning = chosen_word.meaning
    if type(meaning) is accido.misc.MultipleMeanings:
        meaning = random.choice(meaning.meanings)
    assert type(meaning) is str

    answer: str = chosen_word._first  # noqa: SLF001

    other_choices = tuple(
        vocab._first  # noqa: SLF001
        for vocab in random.sample(
            vocab_list,
            # minus one as the chosen word is already in the question
            number_multiplechoice_options - 1,
        )
    )

    choices: list[str] = [answer, *other_choices]
    random.shuffle(choices)

    return MultipleChoiceEngToLatQuestion(
        prompt=meaning, answer=answer, choices=tuple(choices)
    )


def _generate_multiplechoice_lattoeng(
    vocab_list: Vocab,
    chosen_word: accido.endings._Word,
    number_multiplechoice_options: int,
) -> MultipleChoiceLattoEngQuestion:
    prompt: str = chosen_word._first  # noqa: SLF001

    chosen_word_meanings: tuple[str, ...]
    if type(chosen_word.meaning) is accido.misc.MultipleMeanings:
        chosen_word_meanings = tuple(chosen_word.meaning.meanings)
    else:
        assert type(chosen_word.meaning) is str
        chosen_word_meanings = (chosen_word.meaning,)

    answer: str = random.choice(chosen_word_meanings)

    possible_choices: list[str] = []
    for vocab in vocab_list:
        current_meaning: Meaning = vocab.meaning
        if type(current_meaning) is str:
            if current_meaning in chosen_word_meanings:
                continue
            possible_choices.append(current_meaning)
        else:
            assert type(current_meaning) is accido.misc.MultipleMeanings

            possible_choices.extend(
                meaning
                for meaning in current_meaning.meanings
                if meaning not in chosen_word_meanings
            )
    choices: list[str] = [
        answer,
        *random.sample(possible_choices, number_multiplechoice_options - 1),
    ]
    random.shuffle(choices)

    return MultipleChoiceLattoEngQuestion(
        prompt=prompt,
        answer=answer,
        choices=tuple(choices),
    )
