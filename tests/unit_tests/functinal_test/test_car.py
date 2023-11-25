import pytest
import allure


@pytest.mark.smoke
@pytest.mark.parametrize("invalid_brand", [123, None, []])
def test_type_brand(get_new_car_params_with_check_type, invalid_brand):
    with pytest.raises(TypeError, match='Brand must be a string'):
        get_new_car_params_with_check_type(invalid_brand, "Camry", 1000)


@pytest.mark.smoke
@pytest.mark.parametrize("invalid_model", [123, None, []])
def test_type_model(get_new_car_params_with_check_type, invalid_model):
    with pytest.raises(TypeError, match='Model must be a string'):
        get_new_car_params_with_check_type("Toyota", invalid_model, 1000)


@pytest.mark.smoke
@pytest.mark.parametrize("invalid_miles", [-123, None, "str", []])
def test_type_miles_limit(get_new_car_params_with_check_type, invalid_miles):
    with pytest.raises(TypeError, match='Miles limit must be a non-negative number'):
        get_new_car_params_with_check_type("Toyota", "Camry", invalid_miles)


@pytest.mark.sanity
@allure.title('sanity test')
def test_start_engine_when_already_running(get_new_car):
    new_car = get_new_car
    new_car.start_engine()
    start_message = new_car.start_engine()
    assert start_message == "Engine is already running."


@pytest.mark.sanity
@allure.title('sanity test')
def test_start_stop_engine(get_new_car):
    new_car = get_new_car
    start_message = new_car.start_engine()
    assert start_message == "Engine started."
    stop_message = new_car.stop_engine()
    assert stop_message == "Engine stopped."


@pytest.mark.sanity
@allure.title('sanity test')
def test_stop_engine_when_already_off(get_new_car):
    new_car = get_new_car
    stop_message = new_car.stop_engine()
    assert stop_message == "Engine is already off."


@pytest.mark.sanity
@allure.title('sanity test')
def test_drive_without_engine_start(get_new_car):
    new_car = get_new_car
    drive_message = new_car.drive(100)
    assert drive_message == "Cannot drive. Engine is off."


@pytest.mark.sanity
@allure.title('sanity test')
def test_drive_with_engine_start(get_new_car_params_with_check_type):
    new_car = get_new_car_params_with_check_type("Toyota", "Camry", 1000)
    new_car.start_engine()
    miles = 100
    drive_message = new_car.drive(miles)
    assert drive_message == f"Driving {miles} miles."


@pytest.mark.sanity
@allure.title('sanity test')
def test_drive_exceeding_miles_limit(get_new_car):
    new_car = get_new_car
    new_car.start_engine()
    drive_message = new_car.drive(12000)
    assert drive_message == "The miles limit has been exceeded"
