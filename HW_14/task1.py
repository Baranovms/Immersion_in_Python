import pytest 
from Personal import *

@pytest.fixture()
def set_up():
    return UserWorkshop()

def test_access_fail_1(set_up):
    with pytest.raises(AccessError, match='Access denied'):
        set_up.login('Nesterov', '1')


def test_access(set_up):
    assert set_up.login('Nesterov', '1') == '5'


def test_access_fail_2(set_up):                                   
    with pytest.raises(LevelError):
        set_up.login('Nesterov', '1')
        set_up.create_user('Fedorov', '1', '3')



if __name__ == '__main__':
    pytest.main(['-v'])