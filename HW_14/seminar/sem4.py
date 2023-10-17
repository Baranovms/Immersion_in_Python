from sem1_2 import clear_text
import pytest

def test_1():
    assert clear_text('text') == 'text'

def test_2():
    assert clear_text('Te...xt') == 'text'

def test_3():
    assert clear_text('TeЯЯЯяяяяxt') == 'text'

def test_4():
    assert clear_text('T..eЯ..ЯЯ.....яяя...яxt') == 'text'

if __name__ == '__main__':
    pytest.main(['-v'])