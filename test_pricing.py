from pricing import calculate_final_price


def test_no_discount():
    assert calculate_final_price(10000, 0) == 10000


def test_negative_price():
    try:
        calculate_final_price(-1000, 10)
        assert False
    except ValueError:
        assert True


def test_invalid_discount():
    try:
        calculate_final_price(10000, 120)
        assert False
    except ValueError:
        assert True
