def init (self):
    self.balance =0
    def check_balance(self):
        return self.balance
    def deposite(self,amount):
        if amount <=0:
            raise ValueError("deposite amount must be positive")
        self.balance += amount
        def withdraw(self,amount):
          if amount <= 0:
              raise ValueError("withdrawal amount must be positive")  
          if amount > self.balance:
             raise ValueError("insufficient funds") 
          self.balance -= amount
          class ATMController:
              def init (self):
                  self.atm = ATM()
                  def get_number(self,prompt):
                     while True:
                         try:
                             number = float(input(prompt))
                             return number 
except ValueError:
print("please enter a valid number")
def display_menu(self):
    print ("\nwelcome to ATM")
    print ("1. check balance")
    print ("2. deposite")
    print ("3. withdraw")
    print ("4 exit")
    def check_balance(self):
        balance =self.atm.check_balance()
        print(f"your balance is {balance}")
        def deposite(self):
            while True:
                try:
                amount = self.get_number("enter the amount to deposite:")
                self.atm.deposite(amount)
                print(f"successfully deposite {amount}")
                break
        except ValueError as error:
print(error)
def withdraw(self):
    while True
    try:
        amount =self.get_number("enter the amount to withdraw: ")
        self.atm.withdraw(amount)
        print(f"successfully withdraw {amount}")
        break
    except ValueError as error:
        print(error)
        def run(self):
            while True:
                self.display_menu()
                choice = input ("please  choose an option :")
                if choice =='1'
                self.check_balance()
                elif choice =='2'
                self.deposite()
                elif choice =='3'
self.withdraw()
elif choice =='4'
print("thank you for using the ATM")
else:
print("invalid choice. please try again")
def main():
    atm = ATMController()
        atm.run()
        if __name__ =="_main_":
        main()
    
               



                         
                              



