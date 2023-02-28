from function import number_to_month, validate_number
import pytest


@pytest.mark.code # pytest -m code
def test_january_input_1():
    input = 1
    excepted_result = "January"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_february_input_2():
    input = 2
    excepted_result = "February"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_March_input_3():
    input = 3
    excepted_result = "March"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_april_input_4():
    input = 4
    excepted_result = "April"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_may_input_5():
    input = 5
    excepted_result = "May"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_june_input_6():
    input = 6
    excepted_result = "June"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_july_input_7():
    input = 7
    excepted_result = "July"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_august_input_8():
    input = 8
    excepted_result = "August"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_september_input_9():
    input = 9
    excepted_result = "September"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_october_input_10():
    input = 10
    excepted_result = "October"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_october_input_11():
    input = 11
    excepted_result = "November"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_october_input_12():
    input = 12
    excepted_result = "December"
    actual_result = number_to_month(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_0():
    input = 0
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_13():
    input = 13
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_minus_10():
    input = -10
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_22():
    input = 22
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_1_1():
    input = 1.1
    excepted_result = "Input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_13_1():
    input = 13.1
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_a():
    input = "a"
    excepted_result = "Input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result


@pytest.mark.validate # pytest -m validate
def test_input_integer_input_char_sharp():
    input = "#"
    excepted_result = "Input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_1_input_1():
    input = 1
    excepted_result = 1
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_12_input_12():
    input = 12
    excepted_result = 12
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_0_5():
    input = 0.5
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_minus_1_5():
    input = -1.5
    excepted_result = "out of range"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_1_5():
    input = 1.5
    excepted_result = "Input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result



