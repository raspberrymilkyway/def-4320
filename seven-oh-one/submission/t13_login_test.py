import pytest
import System
import RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

#13. tests login - user DNE (fails)
def test_login_user_dne(grading_system):
    username = 'ggdude'
    password = 'nopass'
    grading_system.login(username, password)
