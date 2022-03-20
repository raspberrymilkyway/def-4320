import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#15. drop_student on a ta
def test_drop_student(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    name = 'cmhbf5'
    course = 'software_engineering'
    grading_system.usr.drop_student(name, course)
    assert course not in grading_system.users[name]['courses']
