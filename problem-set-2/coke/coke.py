def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin_inserted = int(input("Insert Coin:"))
        if check_valid_coin(coin_inserted):
            amount_due -= coin_inserted

    print("Change Owed:", amount_due * -1)


def check_valid_coin(coin):
    return coin == 5 or coin == 10 or coin == 25


main()

