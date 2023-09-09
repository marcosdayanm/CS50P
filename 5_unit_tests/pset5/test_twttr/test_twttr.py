from twttr import shorten

def test_a():
    assert shorten('Alma') == 'lm'
    assert shorten('Holaaaa') == 'Hl'

def test_spaces():
    assert shorten('Hi how are you') == 'H hw r y'
    assert shorten('My name is Marcos') == 'My nm s Mrcs'

def test_large_words():
    assert shorten('Ferrocarril') == 'Frrcrrl'
    assert shorten('Paranguaricutirimicuaro') == 'Prngrctrmcr'

def test_numbers_punct():
    assert shorten('I\'m 20 years old!') == '\'m 20 yrs ld!'
    assert shorten('How are you?') == 'Hw r y?'