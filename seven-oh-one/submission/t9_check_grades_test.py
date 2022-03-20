import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#9. check_grades        ()
def test_check_grades(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(username, password)

    course = 'software_engineering'
    x = grading_system.usr.check_grades(course)

    grades = []
    for each in grading_system.users[username]['courses'][course]:
        grades.append([each, grading_system.users[username]['courses'][course][each]['grade']])

    assert grades == x
