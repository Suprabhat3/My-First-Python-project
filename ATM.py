class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.menu()
    def menu(self):
        user_input = input("""Hello, how do you like to proceed
                        1.create pin
                        2.deposit money
                        3.withdraw money
                        4.check balance
                        5.exit
                        :- """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.depostit()    
        elif user_input == '3':
            self.Withdraw()
        elif user_input == '4':
            self.Check_balance()   
        else:
            print("thank you for using our Atm")  
    def create_pin(self):
        self.__pin = input("Enter your pin :")
        print("Pin set successfully")
        self.menu() 
    def depostit(self):
        temp = input("Enter your pin :") 
        if temp == self.__pin:
            amount = int(input("Enter your amount :"))        
            self.__balance = self.__balance + amount
            print("Amount deposit successfully")
        else:
            print("Invalid pin")
        self.menu()    
    def Withdraw(self):
        temp = input("Enter your pin :") 
        if temp == self.__pin:
            amount = int(input("Enter your amount :"))
            if amount <= self.__balance:
               self.__balance = self.__balance-amount       
               print("Amount withdraw successfully") 
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin") 
        self.menu()       
    def Check_balance(self):
        temp = input("Enter your pin :") 
        if temp == self.__pin:         
            print(self.__balance)
        else:
           print("Invalid pin")
        self.menu() 