from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birth_date_str = input("Date of Birth: ")
    try:
        birth_date = parse_date(birth_date_str)
    except ValueError:
        sys.exit("Invalid date format")

    today = date.today()
    minutes = calculate_age_in_minutes(birth_date, today)

    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def parse_date(date_str):
    return date.fromisoformat(date_str)


def calculate_age_in_minutes(birth_date, current_date):
    delta = current_date - birth_date
    return int(delta.total_seconds() / 60)


if __name__ == "__main__":
    main()
