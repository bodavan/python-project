def add(x,y):
    return x +y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divition(x,y):
    return x / y

print("select what do you want to do?")
print(" 1. add \n 2. subtraction \n 3. multiplicaton \n 4. divition")

while True:
    choice = input("what's your operation? 1 or 2 or 3 or 3. \n >>> ")
    if choice in('1','2','3','4'):
        num1 = int(input("Enter your first number : "))
        num2 = int(input("Enter your sescond number : "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3' :
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4' :
            print(num1, "/", num2, "=", divition(num1, num2))

        another= input('do you want to calculate another? yes or no \n >>>')
        if another == "no":
            break
    else:
        print("invaild Input. \n try to select 1-4")

# finish