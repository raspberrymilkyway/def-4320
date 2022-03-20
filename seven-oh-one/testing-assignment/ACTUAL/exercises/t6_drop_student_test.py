import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#6. drop_student        (passes)
def test_login(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    name = 'yted91'
    course = 'software_engineering'
    grading_system.usr.drop_student(name, course)
    assert course not in grading_system.users[name]['courses']
