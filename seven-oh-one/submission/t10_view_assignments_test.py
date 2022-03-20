import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#10. view_assignments   (fails - redefines "course" to only be comp_sci)
def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)

    course = 'databases'
    a = grading_system.courses[course]['assignments']
    assignments = []
    for each in a:
        assignments.append([each, a[each]['due_date']])
    
    assert assignments == grading_system.usr.view_assignments(course)
