from numb3rs import validate


def testformat():
    assert validate('29.8.41') == False
    assert validate('1.32.95.18.74') == False
    assert validate('1.1.1.1.1') == False
    assert validate('0.74.23.3279') == False
    assert validate('.49.23.79') == False
    assert validate('10.4.128.dog') == False
    assert validate('hi.how.are.you') == False
    assert validate('Hey there') == False



def testip():
    assert validate('111.3.55.2') == True
    assert validate('151.22.31.0') == True
    assert validate('324.322.3.105') == False
    assert validate('4.45.555.200') == False


