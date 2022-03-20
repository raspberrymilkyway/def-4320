import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#7. submit_assignment   (fails - is always on time, regardless of date)
def test_submit_assignment(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(username, password)

    course = 'cloud_computing'
    assignment = 'assignment1'
    submission = 'bwah bwah bwah'
    submission_date = '3/22/22'
    grading_system.usr.submit_assignment(course, assignment, submission, submission_date)
    temp = grading_system.users[username]['courses'][course][assignment]
    assert submission in temp['submission'] and submission_date in temp['submission_date'] and temp['ontime'] == False
