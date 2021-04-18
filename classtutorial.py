class Budget:

    """
    A simple python app that implements Budgetting of Food, Clothing and Entertainment with the features:
    1. Deposit
    2. Check balance
    3. Withdrawal
    4. Transfer
    """   
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def categories(self):
        print("\nAvailable categories are: ")
        print ("""
        1. Clothing
        2. Food
        3. Entertainment
        """)   
    

    def getCategory(self):
        while(True):
            try:
                option = input("\nEnter your category or 'q' to quit: ")
                if (option == '1'):
                    option = 1
                    break
                elif(option == '2'):
                    option = 2
                    break
                elif (option == '3'):
                    option = 3
                    break
                elif(option == 'q'):
                    option = 'q'
                    break
                else:
                    print("Wrong input. Please try again")    
                
            except:
                print("A number is required")

        print(f"You selected {option} option")                
        return option
            
                
    
    def setTransaction(self):
        print ("""\nFor this category, you can:
        1. Deposit
        2. Check balance
        3. Withdraw
        4. Transfer\n
            """)

    def deposit(self):
        while(True):
            try:            
                deposit_amount = int(input("Enter amount to be deposited: "))
                self.amount += deposit_amount        
                print("Deposit successful!!!")
                print("Your balance is:", self.amount)
                end_of_processing = input("\nDo you want to perform another transaction?(y/n)\n")
                if end_of_processing == 'n':
                    break
                else:
                    self.getCategory()
            except:
                print("Numbers are the only allowed input")
            
        
            
            
    def check_balance(self):        
        while(True):
            print(f"\nYour balance is ${self.amount}") 
            end_of_processing = input("\nDo you want to perform another transaction?(y/n)\n")
            if end_of_processing == 'n':
                break
            else:
                self.getCategory()
            
            
    def withdraw(self):
        while (True):
            try:
                withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
                if(withdrawal_amount > self.amount):
                    print("Insufficient funds")
                else:            
                    new_amount = self.amount - withdrawal_amount
                    print("Withdrawal Successful!!!")
                    print(f"Your balance is ${new_amount} ")
                    end_of_processing = input("\nDo you want to perform another transaction?(y/n)\n")
                    if end_of_processing == 'n':
                        break
                    else:
                        self.getCategory()                   
            except:
                print("Numbers are needed")
        
            
            
    def transfer(self):     
        while(True):
            category_option = input("Enter the category you want to transfer to: ")
            if(category_option == self.category):
                print("Enter a different category")
                print("Transaction denied!!!")
            else:
                print("You are transfering your ", self.category, " budget")
                category = self.category
                amount = self.amount
                print("\n", category)                
                transfer_amount = int(input("\nEnter the amount you want to transfer: "))
                if(transfer_amount > self.amount):
                    print("Enter a transfer amount within your budget")
                else:
                    new_amount = self.amount - transfer_amount
                    print ("\nTransfer successful!!!\n")
                    print(f"Your balance is:${new_amount}")
                    end_of_processing = input("\nDo you want to perform another transaction?(y/n)\n")
                    if end_of_processing == 'n':
                        break
                    else:
                        self.getCategory()                   
        
category1 = Budget("Clothing", 3000)
category2 = Budget("Food", 2000)
category3 = Budget("Entertainment", 5000)


category1.categories()
option = category1.getCategory()


if(option == 1):
    category1.categories()
    category1.setTransaction()

    transaction = input("Enter an option: ")
    if(transaction == '1'):
        print("\nTransaction is: Deposit")        
        category1.deposit()
    elif(transaction == '2'):
        print("\nTransaction is: Balance check")
        print(f"Your Clothing balance is ${category1.check_balance()}")
    elif(transaction == '3'):
        print("\nTransaction is: Withdrawal")
        category1.withdraw()
    elif(transaction == '4'):
        print("\nTransaction is: Transfer")
        category1.categories()
        category1.transfer()

if(option == 2):
    category2.setTransaction()

    transaction = input("Enter an option: ")
    if(transaction == '1'):
        print("\nTransaction is: Deposit")        
        category2.deposit()
    elif(transaction == '2'):
        print("\nTransaction is: Balance check")
        print(f"Your Food Budget balance is ${category2.check_balance()}")
    elif(transaction == '3'):
        print("\nTransaction is: Withdrawal")
        category2.withdraw()
    elif(transaction == '4'):
        print("\nTransaction is: Transfer")
        category2.categories()
        category2.transfer()


if(option == 3):
    category3.setTransaction()
    transaction = input("Enter an option: ")
    if(transaction == '1'):
        print("\nTransaction is: Deposit")        
        category3.deposit()
    elif(transaction == '2'):
        print("\nTransaction is: Balance check")
        print(f"Your Entertainment Budget balance is ${category3.check_balance()}")
    elif(transaction == '3'):
        print("\nTransaction is: Withdrawal")
        category3.withdraw()
    elif(transaction == '4'):
        print("\nTransaction is: Transfer")
        category3.categories()
        category3.transfer()
elif option == 'q':
    print("\nThanks for using our app today. Don't forget to give us an awesome grade \N{grinning face}")

