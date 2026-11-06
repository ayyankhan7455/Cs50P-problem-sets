def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    for _ in range(100):
        if amount_due <= 0:
            break
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in accepted_coins:
            amount_due -= coin
    print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
