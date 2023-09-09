from plates import is_valid

def test_lett_num():
    assert is_valid('3D443') == False
    assert is_valid('3DK4W') == False
    assert is_valid('DK456') == True
    assert is_valid('DK45P') == False

def test_length():
    assert is_valid('DK456678') == False
    assert is_valid('D') == False
    assert is_valid('5') == False

def test_symbols():
    assert is_valid('DE34!') == False
    assert is_valid('?D450') == False
    assert is_valid('WD4.50') == False

def test_onlynums():
    assert is_valid('EF456') == True
    assert is_valid('EFF4F6') == False
    assert is_valid('EF4T6') == False
