import random
import emojis
import time 
t = 1
user_credit = 1.00


while True:
   
    symbols = ["🍒", "🍋","🍊","⭐","💀"]

    spin1 = random.choice(symbols)
    spin2 = random.choice(symbols)
    spin3 = random.choice(symbols)
    ask = input("do you want to spin?")

    if ask == "yes":
        user_credit = user_credit - 0.20
        print(spin1,spin2,spin3)

        if spin1 == spin2 or spin1 == spin3:
            print("you have won 50p!")
            user_credit = user_credit + 0.30

        if spin2 == spin3:
            print("you have won 50p!")
            user_credit = user_credit + 0.30
            
        if spin1 != spin2 != spin3:
            print("you have lost")