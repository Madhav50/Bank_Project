# import banking_transactions
import banking_transactions

val = True
print("*************************")
print("Hello welcome to the bank")
print("*************************")
while val:

    print(
        "Here are your options: \n1. CREATE ACCOUNT\n2. DELETE ACCOUNT\n3. MODIFY ACCOUNT\n4. DEPOSIT\n5. WITHDRAW\n6. CHECK BALANCE\n7. EXIT")
    options = int(input("Enter Option: "))
    if options == 1:
        banking_transactions.create_account()


    elif options == 2:
        banking_transactions.delete_account()


    elif options == 3:
        banking_transactions.modify_account()


    elif options == 4:
        banking_transactions.deposit()


    elif options == 5:
        banking_transactions.withdraw()


    elif options == 6:
        banking_transactions.check_balance()


    elif options == 7:
        print("Bye!")
        val = False
