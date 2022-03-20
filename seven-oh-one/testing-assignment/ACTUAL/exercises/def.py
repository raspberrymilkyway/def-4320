import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#
def test_login(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)
