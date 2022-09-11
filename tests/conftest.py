from typing import Any


def pytest_generate_tests(metafunc: Any) -> None:
	""" Custom parametrisation scheme """
	function_name = metafunc.function.__name__
	function_scenarios = getattr(metafunc.cls, f"{function_name}_scenarios")
	function_params = [key for key in function_scenarios[0]]
	function_values = [scenario.values() for scenario in function_scenarios]
	ids_list=[sc.get("description") for sc in function_scenarios]

	metafunc.parametrize(function_params, function_values, ids=ids_list, scope="class")
