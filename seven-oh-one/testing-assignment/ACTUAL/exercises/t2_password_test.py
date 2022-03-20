import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#2. check_password     (passes)
def test_password(grading_system):
    username = 'goggins'
    password = 'augurrox'
    x = grading_system.check_password(username, password)
    assert x == True
