import pytest
import System
import Staff

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


#1. login test          (passes)
def test_login(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)
    assert grading_system.usr.name == 'goggins'

#2. check_password      (passes)
#commented out tests also work. you said you wanted 10 tests but i'm submitting all work.
def test_check_password(grading_system):
    username = 'goggins'
    password = 'augurrox'
    x = grading_system.check_password(username, password)
    assert x == True

#def test_password_1(grading_system):
#    username = 'saab'
#    password = 'boomr345'
#    x = grading_system.check_password(username, password)
#    assert x == True

#def test_password_2(grading_system):
#    username = 'yted91'
#    password = 'imoutofpasswordnames'
#    x = grading_system.check_password(username, password)
#    assert x == True

#def test_password_2(grading_system):
#    username = 'yted91'
#    password = 'imnames'
#    x = grading_system.check_password(username, password)
#    assert x == False

#3. change_grade        (fails - sets grade to 0)
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

#5. add_student         (fails - self.name should be name in add_student)
def test_add_student(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    name = 'akend3'
    course = 'software_engineering'
    grading_system.usr.add_student(name, course)
    assert course in grading_system.users[name]['courses']

#6. drop_student        (passes)
def test_drop_student(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)

    name = 'yted91'
    course = 'software_engineering'
    grading_system.usr.drop_student(name, course)
    assert course not in grading_system.users[name]['courses']

#7. submit_assignment   (passes)
def test_submit_assignment(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(username, password)

    course = 'cloud_computing'
    assignment = 'assignment1'
    submission = 'bwah bwah bwah'
    submission_date = '13/22/22'
    grading_system.usr.submit_assignment(course, assignment, submission, submission_date)
    temp = grading_system.users[username]['courses'][course][assignment]
    assert submission in temp['submission'] and submission_date in temp['submission_date']

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

#10. view_assignments   (fails - redefines "course" to only be comp_sci)
def test_view_assignments(grading_system):
    pass

#######

#1. ---
def temp1():
    pass

#2. ---
def temp2():
    pass

#3. ---
def temp3():
    pass

#4. ---
def temp4():
    pass

#5. ---
def temp5():
    pass
