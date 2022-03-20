import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#3. change_grade    (fails - sets grade to 0 instead of specified
#                       expected grade)
def test_change_grade(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    student = 'akend3'
    assignment = 'assignment1'
    course = 'databases'
    grade = 70
    grading_system.usr.change_grade(student, course, assignment, grade)

    assert grade == grading_system.users[student]['courses'][course][assignment]['grade']
