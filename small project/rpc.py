# type 1

import random
while True:
    def start():
        you = input("Enter your choice ,'rock','paper','scissors' \n >>> ")
        computer = random.choice(['rock', 'paper', 'scissors'])

        if you == computer:
            print("its a tie")
        if win(you,computer):
            print('you win')
        elif win(computer,you):
            print('computer win')

    def win(player,opponent):
        if (player == 'paper' and opponent == 'rock') or \
            (player == "scissors" and opponent == 'paper') or \
            (player == "rock" and opponent == "scissors"):
             return True
    start()

    ask = input("do you want to play again? -'yes' or - 'no'")
    if ask == "no":
        break

### another way

import random
while True:
    print("whats your choice? 'rock','paper','scissors'")
    choice = input('>>>')
    while choice not in choice:
        print(input('enter valid choice: '))
    print('your choice is - ',choice)
    print("now it's computer turn.")
    com_choice = random.choice(['rock','paper','scissor'])
    print("computer choice is -",com_choice)
    if choice == com_choice:
        print("it's tie")
    if ((choice == 'rock' and com_choice == 'paper')or \
            (choice == 'paper' and com_choice == 'rock')):
        win = 'paper'
    elif ((choice == 'rock' and com_choice == 'scissor')or \
            (choice == 'scissor' and com_choice == 'rock')):
        win = 'rock'
    else:
        win = 'scissor'
    if win == choice:
        print('you win')
    else:
        print('computer win')
    ask = input("do you want to play again ? 'yes' or 'no'\n >>")
    while ask not in ask:
        print("enter 'yes' or 'no' >")
    if ask == "no" :
        break

### another way -3

import random
print('welcome to rock, paper, scissors. whats your choice?\n ')
you_win = 0
com_win = 0
choice = ['rock','paper','scissors']
while True:
    com_choice = random.choice(choice)
    your_choice = input('Enter your choice :')
    while your_choice not in choice:
        your_choice = input('its not valid. again enter >>>')
    print('your choice is : ',your_choice)
    print('computer choice is: ',com_choice)

    if your_choice == 'rock':
        if com_choice == 'rock':
            print('> its tie!')
        elif com_choice == 'scissors':
            print('> you win')
            you_win += 1
        elif com_choice == 'paper':
            print('> you lose')
            com_win += 1
    elif your_choice == 'paper':
        if com_choice == 'paper':
            print('> its tie')
        elif com_choice == 'rock':
            print('> you win')
            you_win += 1
        elif com_choice == 'scissors':
            print('> you lose')
            com_win += 1
    elif your_choice == 'scissors':
        if com_choice == 'rock':
            print('> you lose')
            com_win += 1
        if com_choice == 'paper':
            print('> you win')
            you_win += 1
        elif com_choice == 'scissors':
            print('> its tie')
    print('you win time : ',you_win)
    print('computer win : ',com_win)
    again = input('do you want to play again? Y or N. >>>')
    if again == 'N' or again == 'n':
        break
print('finish')
