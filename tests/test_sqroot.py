from sqrt_engine import sqroot

def test_perfect_square():
    assert sqroot(4).startswith("2.")
    assert sqroot(169).startswith("13.")
    assert sqroot(10000).startswith("100.")

def test_imperfect_square():
    result = sqroot(2, places=6)
    assert result.startswith("1.4142")

def test_zero_and_one():
    assert sqroot(0).startswith("0.")
    assert sqroot(1).startswith("1.")

def test_high_precision():
    result = sqroot(2, places=50)
    assert len(result.split('.')[1]) >= 50

def test_negative_input():
    try:
        sqroot(-1)
        assert False
    except ValueError:
        assert True

if __name__ == "__main__":
    print("Running sqroot() tests...")
    test_perfect_square()
    test_imperfect_square()
    test_zero_and_one()
    test_high_precision()
    test_negative_input()
    print("All tests passed.")
