import pytest
from tests.unit_tests.car import Car


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )


@pytest.fixture()
def get_new_car():
    new_car = Car('Hyundai', 'i30', 10000)
    return new_car


@pytest.fixture
def get_new_car_params_with_check_type():
    def __inner_new_car(brand, model, miles_limit):
        if not isinstance(brand, str):
            raise TypeError('Brand must be a string')
        elif not isinstance(model, str):
            raise TypeError('Model must be a string')
        elif not isinstance(miles_limit, (int, float)) or miles_limit < 0:
            raise TypeError('Miles limit must be a non-negative number')
        else:
            new_car = Car(brand, model, miles_limit)
        return new_car

    return __inner_new_car
