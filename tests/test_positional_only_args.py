from typing import Callable

import pytest

from validargs.validargs import validated, Validator
from validargs.exceptions import ValidationError
from tests import validators


class TestPositionalOnlyArgumentsNoValidatorsNoDefaults:
    """ Tests Positional arguments, without validators and without default values """

    @validated
    def arguments_without_defaults(
        boolean: bool,
        number_1: int,
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_without_defaults,
            description='Both positional arguments are provided',
            positional_arguments=[False, 1],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_without_defaults,
            description='One POSITIONAL_ONLY argument is missing',
            positional_arguments=[False],
            keyword_arguments={},
            expected_received_arguments=None,
            raised_exception=TypeError,
        )
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


class TestPositionalOnlyArgumentsNoValidatorsDefaults:
    """ Tests Positional arguments, without validators and with default values """

    @validated
    def arguments_with_defaults(
        boolean: bool = False,
        number_1: int = 1,
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_defaults,
            description='Both positional arguments are provided',
            positional_arguments=[False, 1],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='One POSITIONAL_ONLY argument is missing and it is assigned the default value',
            positional_arguments=[False],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_defaults,
            description='Both positional arguments are missing and are assigned the default value',
            positional_arguments=[],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
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


class TestPositionalOnlyArgumentsValidatorsNoDefaults:
    """ Tests Positional arguments, with validators but without default values """

    @validated
    def arguments_with_validators_without_defaults(
        boolean: bool = Validator(validators.boolean),
        number_1: int = Validator(validators.positive_number),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1
        )

        return received_arguments

    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='Both positional arguments are provided with valid values',
            positional_arguments=[False, 1],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='First positional argument is provided with invalid value',
            positional_arguments=[0, 1],
            keyword_arguments={},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='Second positional argument is provided with invalid value',
            positional_arguments=[False, -1],
            keyword_arguments={},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='One POSITIONAL_ONLY argument is missing and the validator does not have default value.',
            positional_arguments=[False],
            keyword_arguments={},
            expected_received_arguments=None,
            raised_exception=TypeError,
        ),
        dict(
            testing_function=arguments_with_validators_without_defaults,
            description='Both positional arguments are missing and the validator does not have default value.',
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


class TestPositionalOnlyArgumentsValidatorsDefaults:
    """ Tests Positional arguments, with validators and with default values """

    @validated
    def arguments_with_validators_with_defaults(
        boolean: bool = Validator(validators.boolean, default_value=False),
        number_1: int = Validator(validators.positive_number, default_value=1),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1
        )

        return received_arguments

    @validated
    def arguments_with_validators_with_defaults_set_to_none(
        boolean: bool = Validator(validators.boolean, default_value=None),
        number_1: int = Validator(validators.positive_number, default_value=None),
    ) -> dict:
        received_arguments = dict(
            boolean=boolean, number_1=number_1
        )

        return received_arguments


    test_arguments_scenarios = [
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='Both positional arguments are provided with valid values',
            positional_arguments=[False, 1],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='First positional argument is provided with invalid value',
            positional_arguments=[0, 1],
            keyword_arguments={},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='Second positional argument is provided with invalid value',
            positional_arguments=[False, -1],
            keyword_arguments={},
            expected_received_arguments=None,
            raised_exception=ValidationError,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='One POSITIONAL_ONLY argument is missing and is assigned the validators default value.',
            positional_arguments=[False],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults,
            description='Both positional arguments are missing and are assigned the validators default value.',
            positional_arguments=[],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=1),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='One POSITIONAL_ONLY argument is missing and is assigned the validators default value None',
            positional_arguments=[False],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=False, number_1=None),
            raised_exception=None,
        ),
        dict(
            testing_function=arguments_with_validators_with_defaults_set_to_none,
            description='Both positional arguments are missing and are assigned the validators default value None.',
            positional_arguments=[],
            keyword_arguments={},
            expected_received_arguments=dict(boolean=None, number_1=None),
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
