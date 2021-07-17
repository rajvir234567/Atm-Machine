class Atm(object):
    def __init__(self, cardNumber, cardPin):
        self.cardNumber = cardNumber
        self.cardPin = cardPin

    def BalanceEnquiry (self):
        print(self.cardNumber, self.cardPin)

    def CashWithdrawl(self):
        print("Your money was successfully removed.")

cardNumber = input("Please enter your card number: ")
cardPin = input("Please enter your card pin: ")

money1 = Atm(cardNumber, cardPin)

money1.BalanceEnquiry()
money1.CashWithdrawl()