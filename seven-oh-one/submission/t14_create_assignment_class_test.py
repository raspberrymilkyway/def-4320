import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#14. create_assignment when a professor does not have access to that class
#                       (fails, since I check that the professor is the same)
def test_create_assignment_class(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    course = 'cloud_computing'
    assignment = 'eeeee'
    due = '13/22/21'
    grading_system.usr.create_assignment(assignment, due, course)
    assert assignment in grading_system.courses[course]['assignments'] and (username in grading_system.courses[course]['professor'] or username in grading_system.courses[course]['ta'])
