import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#11. change_grade (ta)   (fails - sets grade to 0 instead of specified
#                       expected grade)
def test_change_grade_ta(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(username, password)

    student = 'hdjsr7'
    assignment = 'assignment1'
    course = 'cloud_computing'
    grade = 50
    grading_system.usr.change_grade(student, course, assignment, grade)

    assert grade == grading_system.users[student]['courses'][course][assignment]['grade']
