#!/usr/bin/env python3

import hashlib  # this library will encrypt the pin 

'''
A Python class named ATM has been created and contained different methods for displaying the ATM menu, 
handling the user's pin, displaying the user balance, performing withdrawals and deposits on the bank account. 
'''
class ATM:
    def __init__(self, pin=1213, balance=1000, pin_attempt=0):
        self.pin= pin
        self.balance= balance
        self.pin_attempt= pin_attempt
    
    def ATM_menu(self, menu_list= [1,2,3,4]):
        while True:
            try:
                menu_selection=int(input("Select a Menu option: \n 1-Balance \n 2-Withdrawal \n 3-Deposit \n 4-Exit"))
                if menu_selection in menu_list:
                    return menu_selection
                else: print("Your entered an invalid menu option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def encrypt_pin(self, pin):
        sha256 = hashlib.sha256()
        sha256.update(pin.encode('utf-8'))
        encrypted_pin = sha256.hexdigest()
        return encrypted_pin
    
    def verify_pin(self, pin):
        encrypted_pin = self.encrypt_pin(pin)
        return encrypted_pin == self.pin
    
    def pin_check(self):
        while self.pin_attempt<2:
            try:
                user_pin= int(input("Type your PIN"))
                if user_pin == self.pin:
                    return True
                else:
                    print("Your PIN is not correct, retry")
                    self.pin_attempt+=1

            except ValueError:
                print("Invalid input. Please enter a number.")
        return False
    
    def withdrawal(self):
            try:
                withdraw_amount= int(input("How much would yo like to withdraw?"))
                if withdraw_amount<=self.balance:
                    self.balance-=withdraw_amount
                    return self.balance
                else:
                    print("Insufficient balance")
            except ValueError:
                print("Incorrect value. Enter an amount to withdraw")

    #ATM Menu option to deposit money
    def deposit(self):
            try:
                deposit_amount= int(input("How much would yo like to deposit?"))
                if deposit_amount<10000:
                    self.balance += deposit_amount
                    return self.balance
            except ValueError:
                print("Incorrect value.Enter an amount to deposit")

    def execute_atm(self):
        if self.pin_check():
            while True:
                user_option = self.ATM_menu()
                if user_option==1:
                    print(f"Your actual balance is: £{self.balance}")
                elif user_option==2:
                    withdrawal_amount=self.withdrawal()
                    print(f"Your new balance is: £{self.balance}")
                elif user_option==3:
                    deposit_amount=self.deposit()
                    print(f"Your new balance is: £{self.balance}")
                else: 
                    print("Transaction terminated. Have a lovely day!")
                 
                    break  
# Instantiate the ATM class and execute the ATM functionality
atm = ATM()
atm.execute_atm()