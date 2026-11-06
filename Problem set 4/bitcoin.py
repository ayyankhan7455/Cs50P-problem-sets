import sys
import requests


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey"
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit()

    total_cost = n * price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
