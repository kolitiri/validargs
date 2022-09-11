from typing import Callable

import pytest

from validargs.validargs import validated, Validator
from validargs.exceptions import ValidationError
from tests import validators


class TestKeywordOnlyArgumentsNoValidatorsNoDefaults:
    """ Tests Keyword only arguments, without validators and without default values """

    @validated
    def arguments_without_defaults(
        *,
        string_1: str,
        string_2: str,
    ) -> dict:
        received_arguments = dict(
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_without_defaults,
            description='Both keyword arguments are provided',
            positional_arguments=[],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='Both keyword arguments are provided with None values',
            positional_arguments=[],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One keyword argument is missing',
            positional_arguments=[],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='Both keyword arguments are missing',
            positional_arguments=[],
            keyword_arguments={},
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


class TestKeywordOnlyArgumentsNoValidatorsDefaults:
    """ Tests Keyword only arguments, without validators and with default values """

    @validated
    def arguments_with_defaults(
        *,
        string_1: str = "default string 1",
        string_2: str = "default string 2",
    ) -> dict:
        received_arguments = dict(
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_defaults,
            description='Both keyword arguments are provided',
            positional_arguments=[],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='Both keyword arguments are provided with None values',
            positional_arguments=[],
            keyword_arguments={'string_1': None, 'string_2': None},
            expected_received_arguments=dict(string_1=None, string_2=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One keyword argument is missing and assigned the default value',
            positional_arguments=[],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments={'string_1': 'default string 1', 'string_2': 'string 2'},
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='Both keyword arguments are missing and are assigned the default values',
            positional_arguments=[],
            keyword_arguments={},
            expected_received_arguments={'string_1': 'default string 1', 'string_2': 'default string 2'},
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


class TestKeywordOnlyArgumentsValidatorsNoDefaults:
    """ Tests Keyword only arguments, with validators but without default values """

    @validated
    def arguments_with_validators_without_defaults(
        *,
        string_1: str = Validator(validators.short_str),
        string_2: str = Validator(validators.short_str),
    ) -> dict:
        received_arguments = dict(
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='Both keyword arguments are provided with valid values',
            positional_arguments=[],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='First keyword argument is provided with invalid value',
            positional_arguments=[],
            keyword_arguments={'string_1': 'This is a very long string and will fail validation', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='Second keyword argument is provided with invalid value',
            positional_arguments=[],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'This is a very long string and will fail validation'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One keyword argument is missing and the validator does not have default value.',
            positional_arguments=[],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='Both keyword arguments are missing and the validator does not have default value.',
            positional_arguments=[],
            keyword_arguments={},
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


class TestKeywordOnlyArgumentsValidatorsDefaults:
    """ Tests Keyword only arguments, with validators and with default values """

    @validated
    def arguments_with_validators_with_defaults(
        *,
        string_1: str = Validator(validators.short_str, default_value='default string 1'),
        string_2: str = Validator(validators.short_str, default_value='default string 2'),
    ) -> dict:
        received_arguments = dict(
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    @validated
    def arguments_with_validators_with_defaults_set_to_none(
        *,
        string_1: str = Validator(validators.short_str, default_value=None),
        string_2: str = Validator(validators.short_str, default_value=None),
    ) -> dict:
        received_arguments = dict(
            string_1=string_1, string_2=string_2
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='Both KEYWORD_ONLY arguments are provided with valid values',
            positional_arguments=[],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'string 2'},
            expected_received_arguments=dict(string_1='string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='First KEYWORD_ONLY argument is provided with invalid value',
            positional_arguments=[],
            keyword_arguments={'string_1': 'This is a very long string and will fail validation', 'string_2': 'string 2'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='Second KEYWORD_ONLY argument is provided with invalid value',
            positional_arguments=[],
            keyword_arguments={'string_1': 'string 1', 'string_2': 'This is a very long string and will fail validation'},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One KEYWORD_ONLY argument is missing and is assigned the validators default value.',
            positional_arguments=[],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(string_1='default string 1', string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='Both KEYWORD_ONLY arguments are missing and are assigned the validators default value.',
            positional_arguments=[],
            keyword_arguments={},
            expected_received_arguments=dict(string_1='default string 1', string_2='default string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One KEYWORD_ONLY argument is missing and is assigned the validators default value None',
            positional_arguments=[],
            keyword_arguments={'string_2': 'string 2'},
            expected_received_arguments=dict(string_1=None, string_2='string 2'),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='Both KEYWORD_ONLY arguments are missing and are assigned the validators default value None.',
            positional_arguments=[],
            keyword_arguments={},
            expected_received_arguments=dict(string_1=None, string_2=None),
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
