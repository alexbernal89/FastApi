import pytest


def test_equal_or_no_equal():
    assert 3 == 3
    assert 3 != 2

def test_is_instance():
    assert isinstance('Hello world', str)
    assert not isinstance("2", int)


def test_boolean():
    validate = True
    assert validate is True
    assert ('hello' == True) is False


def test_type():
    assert type('Hello' is str)
    assert type(2 is int)
    assert type('Hello' is not int)


def test_greater_and_less_than():
    assert 7 > 4
    assert 4 < 6

def test_list():
    my_list = [1, 2, 3, 4, 5, 6]
    any_list = [False, False]
    assert 1 in my_list
    assert 7 not in my_list
    assert all(my_list)
    assert not any(any_list)


class Student:
    def __init__(self, first_name:str, last_name: str, major: str, year:int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year



@pytest.fixture
def default_employee():
    return Student('Alex', 'Bernal', 'Electronic Engenier', 3)

def test_initialization_student(default_employee):
    assert default_employee.first_name == 'Alex', 'First name should be Alex'
    assert default_employee.last_name == 'Bernal', 'Last name should be Bernal'
    assert default_employee.major == 'Electronic Engenier'
    assert default_employee.year == 3
