#A program to generate random lottery Tickets.
digit = input("Enter the number of digits of ticket-number you want create:-")
num = input("Enter the number of tickets you want to create:-")
import random
for i in range(int(int(num)+1)):
    x = random.random()
    print(int(x*10**int(digit)))





