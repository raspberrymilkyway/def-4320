import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#8. check_ontime        (fails - always returns True)
def test_check_ontime(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(username, password)

    course = 'databases'
    assignment = 'assignment2'
    submission_date = grading_system.users[username]['courses'][course][assignment]['submission_date']
    due_date = grading_system.courses[course]['assignments'][assignment]['due_date']

    x = grading_system.usr.check_ontime(submission_date, due_date)
    assert grading_system.users[username]['courses'][course][assignment]['ontime'] == x
