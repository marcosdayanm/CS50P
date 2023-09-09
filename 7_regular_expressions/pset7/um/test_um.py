from um import count


def test_counter():
    assert count('Hello, um, my, um name is, um Marcos Dayan') == 3
    assert count('Hey how are you? nice to meet you') == 0
    assert count('Hello, um, what is your um... name?') == 2


def test_tricks():
    assert count('um umm UM um... UM?') == 4
    assert count('Hey Marcos, um, it was very yummy!') == 1
    assert count('yummy umbrella tumor forum') == 0
