from typing import Callable

import pytest

from validargs.validargs import validated, Validator
from validargs.exceptions import ValidationError
from tests import validators


class TestMixedArgumentsNoValidatorsNoDefaults:
    """ Tests mixed arguments (positional or not), without validators and without default values """

    @validated
    def arguments_without_defaults(
        boolean: bool,
        number_1: int,
        /,
        number_2: int,
        number_3: int,
        *,
        string_1: str,
        string_2: str,
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[False, 1],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[None, None, None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[None, None, None],
            keyword_arguments={'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[None, None],
            keyword_arguments={'number_2': None, 'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One POSITIONAL_ONLY argument is missing',
            positional_arguments=[False],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One KEYWORD_ONLY argument is missing',
            positional_arguments=[False, 1],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is missing',
            positional_arguments=[False, 1],
            keyword_arguments={'number_3': 3, 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
    ]
    def test_arguments(
        self,
        description: str,
        testing_function: Callable,
        positional_arguments: list,
        keyword_arguments: dict,
        expected_received_arguments: dict,
        raised_exception: Exception,
    ) -> None:

        if raised_exception:
            with pytest.raises(raised_exception):
                testing_function(*positional_arguments, **keyword_arguments)
        else:
            received_arguments = testing_function(*positional_arguments, **keyword_arguments)
            assert received_arguments == expected_received_arguments


class TestMixedArgumentsNoValidatorsDefaults:
    """ Tests mixed arguments (positional or not), without validators and with default values """

    @validated
    def arguments_with_defaults(
        boolean: bool = False,
        number_1: int = 1,
        /,
        number_2: int = 2,
        number_3: int = 3,
        *,
        string_1: str = "default string 1",
        string_2: str = "default string 2",
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[False, 1],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[None, None, None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[None, None, None],
            keyword_arguments={'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[None, None],
            keyword_arguments={'number_2': None, 'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One POSITIONAL_ONLY argument is missing and is assigned the default value',
            positional_arguments=[False],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One KEYWORD_ONLY argument is missing and is assigned the default value',
            positional_arguments=[False, 1],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='default string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is missing and is assigned the default value',
            positional_arguments=[False, 1],
            keyword_arguments={'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
    ]
    def test_arguments(
        self,
        description: str,
        testing_function: Callable,
        positional_arguments: list,
        keyword_arguments: dict,
        expected_received_arguments: dict,
        raised_exception: Exception,
    ) -> None:

        if raised_exception:
            with pytest.raises(raised_exception):
                testing_function(*positional_arguments, **keyword_arguments)
        else:
            received_arguments = testing_function(*positional_arguments, **keyword_arguments)
            assert received_arguments == expected_received_arguments


class TestMixedArgumentsValidatorsNoDefaults:
    """ Tests mixed arguments (positional or not), with validators but without default values """

    @validated
    def arguments_with_validators_without_defaults(
        boolean: bool = Validator(validators.boolean),
        number_1: int = Validator(validators.positive_number),
        /,
        number_2: int = Validator(validators.positive_number),
        number_3: int = Validator(validators.positive_number),
        *,
        string_1: str = Validator(validators.short_str),
        string_2: str = Validator(validators.short_str),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[False, 1],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[None, None, None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[None, None, None],
            keyword_arguments={'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[None, None],
            keyword_arguments={'number_2': None, 'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_ONLY argument is provided with invalid value',
            positional_arguments=[False, -1, 2, 3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One KEYWORD_ONLY argument is provided with invalid value',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'This is a very long string and will fail validation', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is provided with invalid value (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[False, 1, 2, -3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is provided with invalid value (POSITIONAL_OR_KEYWORD ones a keyword)',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'number_3': -3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),

        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One KEYWORD_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
    ]
    def test_arguments(
        self,
        description: str,
        testing_function: Callable,
        positional_arguments: list,
        keyword_arguments: dict,
        expected_received_arguments: dict,
        raised_exception: Exception,
    ) -> None:

        if raised_exception:
            with pytest.raises(raised_exception):
                testing_function(*positional_arguments, **keyword_arguments)
        else:
            received_arguments = testing_function(*positional_arguments, **keyword_arguments)
            assert received_arguments == expected_received_arguments


class TestMixedArgumentsValidatorsDefaults:
    """ Tests mixed arguments (positional or not), with validators and with default values """

    @validated
    def arguments_with_validators_with_defaults(
        boolean: bool = Validator(validators.boolean, default_value=False),
        number_1: int = Validator(validators.positive_number, default_value=1),
        /,
        number_2: int = Validator(validators.positive_number, default_value=2),
        number_3: int = Validator(validators.positive_number, default_value=3),
        *,
        string_1: str = Validator(validators.short_str, default_value='default string 1'),
        string_2: str = Validator(validators.short_str, default_value='default string 1'),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    @validated
    def arguments_with_validators_with_defaults_set_to_none(
        boolean: bool = Validator(validators.boolean, default_value=None),
        number_1: int = Validator(validators.positive_number, default_value=None),
        /,
        number_2: int = Validator(validators.positive_number, default_value=None),
        number_3: int = Validator(validators.positive_number, default_value=None),
        *,
        string_1: str = Validator(validators.short_str, default_value=None),
        string_2: str = Validator(validators.short_str, default_value=None),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[False, 1],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[None, None, None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as positional and keyword)',
            positional_arguments=[None, None, None],
            keyword_arguments={'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided with None values (POSITIONAL_OR_KEYWORD both as keyword)',
            positional_arguments=[None, None],
            keyword_arguments={'number_2': None, 'number_3': None, 'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, number_2=None, number_3=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_ONLY argument is provided with invalid value',
            positional_arguments=[False, -1, 2, 3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One KEYWORD_ONLY argument is provided with invalid value',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'This is a very long string and will fail validation', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is provided with invalid value (POSITIONAL_OR_KEYWORD ones a positional)',
            positional_arguments=[False, 1, 2, -3],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is provided with invalid value (POSITIONAL_OR_KEYWORD ones a keyword)',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'number_3': -3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One KEYWORD_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='default string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_OR_KEYWORD argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=None, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One KEYWORD_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1=None, string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One POSITIONAL_OR_KEYWORD argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=None, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
    ]
    def test_arguments(
        self,
        description: str,
        testing_function: Callable,
        positional_arguments: list,
        keyword_arguments: dict,
        expected_received_arguments: dict,
        raised_exception: Exception,
    ) -> None:

        if raised_exception:
            with pytest.raises(raised_exception):
                testing_function(*positional_arguments, **keyword_arguments)
        else:
            received_arguments = testing_function(*positional_arguments, **keyword_arguments)
            assert received_arguments == expected_received_arguments


class TestMixedArgumentsInCombinations:
    """ Tests mixed arguments (positional or not), in combinations with or without validators """

    @validated
    def arguments_with_or_without_validators_with_or_without_defaults_1(
        boolean: bool = False,
        number_1: int = Validator(validators.positive_number, default_value=1),
        /,
        number_2: int = Validator(validators.positive_number),
        number_3: int = Validator(validators.positive_number, default_value=3),
        *,
        string_1: str,
        string_2: str = Validator(validators.short_str, default_value='default string'),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    @validated
    def arguments_with_or_without_validators_with_or_without_defaults_2(
        boolean: bool,
        number_1: int = Validator(validators.positive_number, default_value=None),
        /,
        number_2: int = 2,
        number_3: int = Validator(validators.positive_number, default_value=3),
        *,
        string_1: str,
        string_2: str = Validator(validators.short_str, default_value='default string'),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    @validated
    def arguments_with_validators_with_invalid_defaults(
        boolean: bool,
        number_1: int = Validator(validators.positive_number, default_value=None),
        /,
        number_2: int = 2,
        number_3: int = Validator(validators.positive_number, default_value=3),
        *,
        string_1: str,
        string_2: str = Validator(validators.short_str, default_value='This is a very long string and it will fail validation'),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1, number_2=number_2,
            number_3=number_3, string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_or_without_validators_with_or_without_defaults_1,
            description='Two positional arguments are missing and are assigned the default values',
            positional_arguments=[],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_or_without_validators_with_or_without_defaults_1,
            description='One KEYWORD_ONLY argument is missing and it does not have default value',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_or_without_validators_with_or_without_defaults_2,
            description='Two positional arguments are missing and one of them does not have default value',
            positional_arguments=[],
            keyword_arguments={'number_2': 2, 'number_3': 3, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_or_without_validators_with_or_without_defaults_2,
            description='One KEYWORD_ONLY argument is missing and it is assigned the default value',
            positional_arguments=[False, 1, 2, 3],
            keyword_arguments={'string_1': 'string 1'},
            expected_received_arguments=dict(boolean=False, number_1=1, number_2=2, number_3=3, string_1='string 1', string_2='default string'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_invalid_defaults,
            description='One KEYWORD_ONLY argument is missing and it is has an invalid default value',
            positional_arguments=[False, 1, 2],
            keyword_arguments={'string_1': 'string 1'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
    ]
    def test_arguments(
        self,
        description: str,
        testing_function: Callable,
        positional_arguments: list,
        keyword_arguments: dict,
        expected_received_arguments: dict,
        raised_exception: Exception,
    ) -> None:

        if raised_exception:
            with pytest.raises(raised_exception):
                testing_function(*positional_arguments, **keyword_arguments)
        else:
            received_arguments = testing_function(*positional_arguments, **keyword_arguments)
            assert received_arguments == expected_received_arguments
