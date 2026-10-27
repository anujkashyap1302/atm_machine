class atm:
    def __init__(self):
        self.balance = 10000
        self.pin = 1234
        print('welcome to atm')
    def card_inserted(self):
        user_card = input(" insert your card: ")
        if user_card== 'card':
            print('card inserted')
            ob.enter_pin()
        else:
            print('invalid card')
    def enter_pin(self):
        user_pin = int(input("enter your pin: "))
        if user_pin == self.pin:
            print('correct pin')
            print("1) check balance\n2) withdraw")
        else:
            print('incorrect pin')