from square import get_square

def test_get_square():
    a = 4
    result = get_square(a)
    if result == 16:
        return "correct Value"
    #assert result == 16    # if it is other then 16 it throws an error
    """
        if result == 16:
        return 'test_passed'
    """

if __name__ == '__main__':
    print(test_get_square())
