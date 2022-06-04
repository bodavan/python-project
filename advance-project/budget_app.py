class budget:
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def deposit(self,amount):
        self.balance = amount
        print('your new balance is ', self.balance, 'add in ', self.name)

    def withdrow(self,amount):

         if self.balance < amount:
             print('********** Transaction Failed ***********')
             print("you don't have sufficient balance")

         else:
             self.balance = self.balance - amount
             print("############ successful transaction ############")
             print("your new balance is ",self.balance ,"in",self.name)

    def get_balance(self):
        print("your balance is ",self.balance,"in",self.name)

    def transfar(self,amount,category):

        if self.name == category.name:
            result = (f"Error!!!\n")
            result += (f"you can't transfar money within the same category.")
            result += (f"you can only transfar money to the another catefory")
            return result

        else:
            if self.balance < amount :
                print("*** Transaction Failed ")
                print("you have insufficient balance")

            else:
                self.balance -= amount
                category.balance += amount

                print("*******  Transaction successful *******")
                print(f"> now you balance is {self.balance} in {self.name} fund")
                print(f"> And in your {category.name} fund you have {category.balance}")


food = budget("food")
clothing = budget("clothing")
entertainment = budget("entertainment")

food.deposit(4000)
clothing.deposit(2000)
entertainment.deposit(1000)

print(clothing.transfar(1000,food))
