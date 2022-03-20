import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#5. add_student     (fails - self.name should just be name in add_student)
def test_add_student(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    name = 'akend3'
    course = 'software_engineering'
    grading_system.usr.add_student(name, course)
    assert course in grading_system.users[name]['courses']
