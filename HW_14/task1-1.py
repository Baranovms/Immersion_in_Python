import pytest
from Personal import *

class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level

# Фикстура для создания объекта User
@pytest.fixture
def user():
    return User("Baranov", 2, 3)

def test_user_name(user):
    assert user.name == "Baranov"

def test_user_id(user):
    assert user.user_id == 2

def test_user_level(user):
    assert user.level == 3

def test_user_object_type(user):
    assert isinstance(user, User)

def test_user_name_type(user):
    assert isinstance(user.name, str)

def test_user_id_type(user):
    assert isinstance(user.user_id, int)

def test_user_level_type(user):
    assert isinstance(user.level, int)
    
    
if __name__ == '__main__':
    pytest.main(['-v'])