import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#4. create_assignment   (passes)
def test_create_assignment(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    assignment = 'freepoints'
    due = '3/19/22'
    course = 'databases'
    grading_system.usr.create_assignment(assignment, due, course)
    assert assignment in grading_system.courses[course]['assignments']
