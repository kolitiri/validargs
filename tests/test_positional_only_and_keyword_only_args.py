from typing import Callable

import pytest

from validargs.validargs import validated, Validator
from validargs.exceptions import ValidationError
from tests import validators


class TestPositionalOnlyAndKeywordOnlyArgumentsNoValidatorsNoDefaults:
    """ Tests Positional only and Keyword only arguments, without validators and without default values """

    @validated
    def arguments_without_defaults(
        boolean: bool,
        number_1: int,
        string_1: str,
        string_2: str,
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1,
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided',
            positional_arguments=[False, 1],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='All arguments are provided with None values',
            positional_arguments=[None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One POSITIONAL_ONLY argument is missing',
            positional_arguments=[False],
            keyword_arguments={'number_2': 2, 'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One keyword argument is missing',
            positional_arguments=[False, 1],
            keyword_arguments={'string_2': 'string 2'},
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


class TestPositionalOnlyAndKeywordOnlyArgumentsNoValidatorsDefaults:
    """ Tests Positional only and Keyword only arguments, without validators and with default values """

    @validated
    def arguments_with_defaults(
        boolean: bool = False,
        number_1: int = 1,
        string_1: str = "default string 1",
        string_2: str = "default string 2",
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1,
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided',
            positional_arguments=[False, 1],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='All arguments are provided with None values',
            positional_arguments=[None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One POSITIONAL_ONLY argument is missing and is assigned the default value',
            positional_arguments=[False],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One keyword argument is missing and is assigned the default value',
            positional_arguments=[False, 1],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='default string 1', string_2='string 2'),
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


class TestPositionalOnlyAndKeywordOnlyArgumentsValidatorsNoDefaults:
    """ Tests Positional only and Keyword only arguments, with validators but without default values """

    @validated
    def arguments_with_validators_without_defaults(
        boolean: bool = Validator(validators.boolean),
        number_1: int = Validator(validators.positive_number),
        string_1: str = Validator(validators.short_str),
        string_2: str = Validator(validators.short_str),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1,
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided',
            positional_arguments=[False, 1],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='All arguments are provided with None values',
            positional_arguments=[None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_ONLY argument is provided with invalid value',
            positional_arguments=[False, -1],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One KEYWORD_ONLY argument is provided with invalid value',
            positional_arguments=[False, 1],
            keyword_arguments={'string_1': 'This is a very long string and will fail validation', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One KEYWORD_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1],
            keyword_arguments={'string_2': 'string 2'},
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


class TestPositionalOnlyAndKeywordOnlyArgumentsValidatorsDefaults:
    """ Tests Positional only and Keyword only arguments, with validators and with default values """

    @validated
    def arguments_with_validators_with_defaults(
        boolean: bool = Validator(validators.boolean, default_value=False),
        number_1: int = Validator(validators.positive_number, default_value=1),
        string_1: str = Validator(validators.short_str, default_value='default string 1'),
        string_2: str = Validator(validators.short_str, default_value='default string 1'),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1,
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    @validated
    def arguments_with_validators_with_defaults_set_to_none(
        boolean: bool = Validator(validators.boolean, default_value=None),
        number_1: int = Validator(validators.positive_number, default_value=None),
        string_1: str = Validator(validators.short_str, default_value=None),
        string_2: str = Validator(validators.short_str, default_value=None),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1,
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided',
            positional_arguments=[False, 1],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='All arguments are provided with None values',
            positional_arguments=[None, None],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(boolean=None, number_1=None, string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_ONLY argument is provided with invalid value',
            positional_arguments=[False, -1],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One KEYWORD_ONLY argument is provided with invalid value',
            positional_arguments=[False, 1],
            keyword_arguments={'string_1': 'This is a very long string and will fail validation', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One KEYWORD_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1='default string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=None, string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One KEYWORD_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False, 1],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(boolean=False, number_1=1, string_1=None, string_2='string 2'),
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
