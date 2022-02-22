class Atm (object):
    def __init__(self,atm_card_number,pin_number,ifsc):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
        self.ifsc = ifsc
    def cashWithdrwal (self):
        amount = input('enter the amount_ ')
        print("ruppees ",amount," cash withdrawl complete ")
    def creditCash (self):
        amount = input('enter the amount_ ')
        print("ruppees ",amount," crediting complete")
number = input("what's your credit card number? ")
pin = input("what's your pin number? ")
ifSc = input("what's your ifsc code? ")
person = Atm(number,pin,ifSc)
question = input("type 'a' if you want to withdraw cash or 'b' if you want to credit cash or 'c' if you want to do nothing_ ")
if question == 'a' :
    person.cashWithdrwal()
elif question == 'b':
    person.creditCash()
else:
    print("bye! ")
