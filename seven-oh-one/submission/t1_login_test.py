import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#1. login test      (passes)
def test_login(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username, password)
    assert grading_system.usr.name == 'goggins'
