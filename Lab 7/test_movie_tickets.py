from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


# ---------- 1. "No crash" fuzz tests (random text and None) ----------

@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        parse_seat(s)
    except Exception as e:
        assert False, f"parse_seat crashed with: {e!r}"


@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        total_price(s)
    except Exception as e:
        assert False, f"total_price crashed with: {e!r}"


@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        average_rating(s)
    except Exception as e:
        assert False, f"average_rating crashed with: {e!r}"


# ---------- 2. Correctness tests for valid input ----------

@given(st.sampled_from("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"),
       st.integers(min_value=1, max_value=999))
def test_parse_seat_valid(row, number):
    assert parse_seat(f"{row}{number}") == (row.upper(), number)


@given(st.lists(st.integers(min_value=0, max_value=100000), min_size=1, max_size=20))
def test_total_price_valid(prices):
    csv = ",".join(str(p) for p in prices)
    assert total_price(csv) == round(sum(prices) * 1.18, 2)


@given(st.lists(st.integers(min_value=1, max_value=5), min_size=1, max_size=30))
def test_average_rating_valid(ratings):
    result = average_rating(" ".join(str(r) for r in ratings))
    assert result is not None
    assert 1 <= result <= 5


# ---------- 3. Known edge cases ----------

def test_known_bad_inputs_rejected():
    assert parse_seat("") is None
    assert parse_seat("H") is None
    assert parse_seat("12") is None
    assert parse_seat("H-3") is None
    assert parse_seat(None) is None
    assert total_price("150,,400") is None
    assert total_price("") is None
    assert total_price("a,b") is None
    assert total_price("-5,10") is None
    assert average_rating("") is None
    assert average_rating("a b") is None
    assert average_rating("9 5") is None
    assert average_rating(None) is None


def test_example_values():
    assert parse_seat("h12") == ("H", 12)
    assert total_price("150,250,400") == 944.0
    assert average_rating("4 5 3") == 4.0