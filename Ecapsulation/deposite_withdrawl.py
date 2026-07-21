class Account:

    def __init__(self):
        self.__number = None
        self.__accountType = None
        self.__balance = 0.0
        self.__transaction_count = 0


    def setNumber(self, number):
        self.__number = number

    def setAccountType(self, accountType):
        self.__accountType = accountType


    def getNumber(self):
        return self.__number

    def getAccountType(self):
        return self.__accountType

    def getBalance(self):
        return self.__balance

    def getTransactionCount(self):
        return self.__transaction_count

    # ---------------- Deposit ----------------

    def deposit(self, amt):
        if amt <= 50000:
            self.__balance += amt
            self.__transaction_count += 1
            print("Amount deposited successfully.")
        else:
            print("Only 50000 can be deposited at one time.")

    # ---------------- Withdrawal ----------------

    def withdrawal(self, amt):
        if self.__transaction_count < 5:

            if amt <= 5000:

                if self.__balance >= amt:
                    self.__balance -= amt
                    self.__transaction_count += 1
                    print("Amount withdrawn successfully.")
                else:
                    print("Insufficient Balance")

            else:
                print("Only 5000 can be withdrawn at one time.")

        else:
            print("Transaction limit is over.")

# ---------------- Main Program ----------------

acc = Account()

acc.setNumber(101)
acc.setAccountType("Saving")

print("Account Number :", acc.getNumber())
print("Account Type :", acc.getAccountType())

acc.deposit(20000)
print("Balance :", acc.getBalance())

acc.withdrawal(3000)
print("Balance :", acc.getBalance())

acc.withdrawal(7000)

acc.deposit(60000)