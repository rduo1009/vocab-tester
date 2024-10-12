#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that generate questions and check answers."""

from __future__ import annotations

import random
from typing import TYPE_CHECKING, Any, Final, Generator

from .. import accido, lego, transfero
from ..accido.misc import Case, Gender, Mood, Number
from .exceptions import InvalidSettingsError
from .question_classes import (
    ParseWordCompToLatQuestion,
    ParseWordLatToCompQuestion,
    PrincipalPartsQuestion,
    QuestionClasses,
    TypeInEngToLatQuestion,
    TypeInLatToEngQuestion,
)
from .rules import filter_endings, filter_questions, filter_words
from .type_aliases import Settings

if TYPE_CHECKING:
    from ..accido.type_aliases import Ending, Meaning
    from .question_classes import Question
    from .type_aliases import Vocab

REQUIRED_SETTINGS: Final[set[str]] = set(Settings.__annotations__.keys())


def _verify_settings(settings: Settings) -> None:
    """Verifies that the settings are valid.

    Parameters
    ----------
    settings : Settings
        The settings to verify.

    Raises
    ------
    InvalidSettingsError
        If the settings are invalid.
    """
    # Convert dictionary keys to a set
    setting_keys: set[str] = set(settings.keys())

    # Compare the sets
    if setting_keys == REQUIRED_SETTINGS:
        return
    unrecognised_settings: set[str] = setting_keys - REQUIRED_SETTINGS
    missing_settings: set[str] = REQUIRED_SETTINGS - setting_keys

    if unrecognised_settings:
        raise InvalidSettingsError(
            f"Unrecognised settings: {", ".join(unrecognised_settings)}"
        )
    if missing_settings:
        raise InvalidSettingsError(
            f"Missing settings: {", ".join(missing_settings)}"
        )


def _pick_ending(
    endings: dict[str, Ending],
) -> tuple[str, Ending]:
    return random.choice(list(endings.items()))


def ask_question_without_sr(
    vocab_list: lego.misc.VocabList, amount: int, settings: Settings
) -> Generator[Question, None, None]:
    """Ask a question about Latin vocabulary.

    Parameters
    ----------
    vocab_list : VocabList
        The vocabulary list to use.
    amount : int
        The number of questions to ask.
    settings : Settings
        The settings to use.

    Yields
    ------
    Question
        The question to ask.
    """
    _verify_settings(settings)
    vocab: Vocab = filter_words(vocab_list, settings)
    filtered_questions: list[QuestionClasses] = filter_questions(settings)

    for _ in range(amount):
        chosen_word: accido.endings._Word = random.choice(vocab)
        filtered_endings: dict[str, Ending] = filter_endings(
            chosen_word.endings, settings
        )
        question_type: QuestionClasses = random.choice(filtered_questions)

        # TODO: if ever using mypyc, make a new variable for every type
        # for now, any type to allow variable to be reused
        output: Any
        match question_type:
            case QuestionClasses.TYPEIN_ENGTOLAT:
                if output := _generate_typein_engtolat(
                    chosen_word, filtered_endings
                ):
                    assert type(output) is TypeInEngToLatQuestion
                    yield output
                else:
                    continue

            case QuestionClasses.TYPEIN_LATTOENG:
                if output := _generate_typein_lattoeng(
                    chosen_word, filtered_endings
                ):
                    assert type(output) is TypeInLatToEngQuestion
                    yield output
                else:
                    continue

            case QuestionClasses.PARSEWORD_LATTOCOMP:
                if output := _generate_parse(chosen_word, filtered_endings):
                    assert type(output) is ParseWordLatToCompQuestion
                    yield output
                else:
                    continue

            case QuestionClasses.PARSEWORD_COMPTOLAT:
                if output := _generate_inflect(chosen_word, filtered_endings):
                    assert type(output) is ParseWordCompToLatQuestion
                    yield output
                else:
                    continue

            case QuestionClasses.PRINCIPAL_PARTS:
                if output := _generate_principal_parts_question(chosen_word):
                    assert type(output) is PrincipalPartsQuestion
                    yield output
                else:
                    continue


def _generate_typein_engtolat(  # noqa: PLR0914, PLR0915
    chosen_word: accido.endings._Word, filtered_endings: dict[str, Ending]
) -> TypeInEngToLatQuestion | None:
    ending_components_key: str
    chosen_ending: Ending
    ending_components_key, chosen_ending = _pick_ending(filtered_endings)

    if type(chosen_ending) is accido.misc.MultipleEndings:
        chosen_ending = random.choice(chosen_ending.get_all())
    assert type(chosen_ending) is str

    # HACK: Uses a private method but there's no alternative
    ending_components: accido.misc.EndingComponents = (
        chosen_word._create_namespace(ending_components_key)  # noqa: SLF001
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
    inflected_meaning: str = random.choice(
        tuple(
            transfero.words.find_inflection(
                word=raw_meaning,
                components=ending_components,
            )
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
                case=Case.ACCUSATIVE,
                number=ending_components.number,
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
        prompt=inflected_meaning,
        main_answer=chosen_ending,
        answers=answers,
    )


def _generate_typein_lattoeng(
    chosen_word: accido.endings._Word, filtered_endings: dict[str, Ending]
) -> TypeInLatToEngQuestion | None:
    chosen_ending: Ending
    _, chosen_ending = _pick_ending(filtered_endings)

    if type(chosen_ending) is accido.misc.MultipleEndings:
        chosen_ending = random.choice(chosen_ending.get_all())
    assert type(chosen_ending) is str

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
                    word=meaning,
                    components=ending_components,
                )
            )

        possible_main_answers.add(
            random.choice(
                tuple(
                    transfero.words.find_inflection(
                        word=main_meaning,
                        components=ending_components,
                    )
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
    chosen_word: accido.endings._Word, filtered_endings: dict[str, Ending]
) -> ParseWordLatToCompQuestion | None:
    if type(chosen_word) is accido.endings.RegularWord:
        return None

    ending_components_key: str
    chosen_ending: Ending
    ending_components_key, chosen_ending = _pick_ending(filtered_endings)

    main_ending_components: accido.misc.EndingComponents = (
        chosen_word._create_namespace(ending_components_key)  # noqa: SLF001
    )

    if type(chosen_ending) is accido.misc.MultipleEndings:
        chosen_ending = random.choice(chosen_ending.get_all())
    assert type(chosen_ending) is str

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
    chosen_word: accido.endings._Word, filtered_endings: dict[str, Ending]
) -> ParseWordCompToLatQuestion | None:
    if type(chosen_word) is accido.endings.RegularWord:
        return None

    ending_components_key: str
    chosen_ending: Ending
    ending_components_key, chosen_ending = _pick_ending(filtered_endings)

    ending_components: accido.misc.EndingComponents = (
        chosen_word._create_namespace(ending_components_key)  # noqa: SLF001
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
            principal_parts = (
                chosen_word.nominative,
                chosen_word.genitive,
            )
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
