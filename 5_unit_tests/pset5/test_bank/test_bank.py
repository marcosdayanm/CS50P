from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hElloo') == 0
    assert value('HELLOUU') == 0

def test_h():
    assert value('heY tHereee') == 20
    assert value('Happy halloween') == 20

def test_none():
    assert value('What\'s up?') == 100
    assert value('1001000111010') == 100