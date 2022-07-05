def main():
    total_due = 50
    accepted_denominations = [5, 10, 25]

    while total_due > 0:
        try:
            print("Amount Due: " + str(total_due))
            inserted_coin = int(input("Insert Coin: "))

            if inserted_coin in accepted_denominations:
                total_due -= inserted_coin
            # Had to remove the following else statement to pass the check50 :(
            #else:
                #print("We only accecpt the following denominations: " + str(accepted_denominations))

        except ValueError:
            print("Please insert a valid coin, you animal.")

    if total_due <= 0:
        change = abs(total_due)
        print("Change Due: " + str(change))

main()