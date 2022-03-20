# ASSIGNMENT 7.01 --- Kylee Willis (kwcnr)

Any file with the format that has "test.py" at the end is a file that is part of my submission. The number at the beginning is the question that test is answering.

### Test 1 - login		(passes)

### Test 2 - check_password 	(passes)

### Test 3 - change_grade	(fails)
Checks grade as a Professor. Does not work - grade is always changed to 0 instead of the specified grade

### Test 4 - create_assignment	(passes)

### Test 5 - add_student	(fails)
Attempts to add a student to a course. Does not work - formatting of adding student is not correct (should be name instead of self.name in the brackets)

### Test 6 - drop_student	(passes)

### Test 7 - submit_assignment 	(fails)
Submits an assignment correctly, but does not check whether the assignment is on time or not correctly - the date specified is always from the "comp_sci" assignment of the same name, if there is one.

### Test 8 - check_ontime	(fails)
Simply returns true, when it is not always. Nothing is checked.

### Test 9 - check_grades	(passes)

### Test 10 - view_assignments	(fails)
Views all assignments within "comp_sci" correctly, but does not get the specified course if it is not comp_sci.

### Test 11 - change_grade	(fails)
Checks grade, but as a TA user. Still fails.

### Test 12 - add_student	(fails)
Adds a student, but as a TA user. Still fails.

### Test 13 - login		(fails)
Tries to login with a user not in the system. Still queries database, doesn't throw an error or anything.

### Test 14 - create_assignment	(fails)
Checks to see if a professor without access to a course can create an assignment. They can. Fails because the instructor listed is not the same, not because the assignment does not exist.

### Test 15 - drop_student	(fails)
Attempts to drop a TA from a course. Does not work - cannot drop TA from a course - but does not throw an error. Also, there should be a way to drop a TA from a course.
