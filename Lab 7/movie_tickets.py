MAX_SEAT_NUMBER = 999
MAX_PRICE = 100000
MIN_RATING = 1
MAX_RATING = 5


def _is_plain_number(text):
    """True only for non-empty strings made of ASCII digits 0-9."""
    return text != "" and text.isascii() and text.isdigit()


def parse_seat(seat):
    """Return (ROW_LETTER, seat_number) or None if the seat is invalid."""
    if not isinstance(seat, str):
        return None
    seat = seat.strip()
    if len(seat) < 2:
        return None
    row, number = seat[0], seat[1:]
    if not (row.isascii() and row.isalpha()):
        return None
    if not _is_plain_number(number) or len(number) > 3:
        return None
    number = int(number)
    if number < 1 or number > MAX_SEAT_NUMBER:
        return None
    return row.upper(), number


def total_price(prices_csv):
    """Return total including 18% GST, or None if the input is invalid."""
    if not isinstance(prices_csv, str):
        return None
    prices = []
    for part in prices_csv.split(','):
        part = part.strip()
        if not _is_plain_number(part) or len(part) > 6:
            return None
        price = int(part)
        if price > MAX_PRICE:
            return None
        prices.append(price)
    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    """Return the average of ratings (1-5), or None if the input is invalid."""
    if not isinstance(ratings, str):
        return None
    parts = ratings.split()
    if not parts:
        return None
    values = []
    for part in parts:
        if not _is_plain_number(part) or len(part) > 2:
            return None
        value = int(part)
        if value < MIN_RATING or value > MAX_RATING:
            return None
        values.append(value)
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    if result is None:
        print("Invalid seat. Use one letter followed by a number, e.g. H12.")
    else:
        print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    if result is None:
        print("Invalid prices. Use whole numbers separated by commas.")
    else:
        print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    if result is None:
        print("Invalid ratings. Use numbers from 1 to 5 separated by spaces.")
    else:
        print("Average Rating:", result)

if __name__ == "__main__":
    main()