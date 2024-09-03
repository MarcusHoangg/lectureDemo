#ex1
'''
rounds=int(input("How many greetings :"))
finished_rounds = 0
while  finished_rounds < rounds :
    print("good morning")
    finished_rounds=finished_rounds+1
'''
import random

#ex2
'''
command=input("enter command:")
while command != "stop":
    print("executing command:"+command)
    command=input("enter command:")
print("execution stopped")
'''
#ex3
'''
import random
dice1=dice2=rolls=0
while (dice1 !=6 or dice2 !=6 ):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    rolls=rolls+1
print("rolled", rolls,"times")
'''
#ex4
'''
first =1
while first<=5:
    second = 1
    while second<=5:
        print(f"{first}times{second}is {first*second:d}")
        second=second+1
        first=first+1
'''
#ex5
'''
command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")
'''
#EX6
'''
command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")
'''

#ex in class
'''
i=1
n=int(input("enter the limit"))
while i <n :
    print("before increament",i)
    i=i+1
print("adios")
'''
#ex3
'''
sum = 0
counter = 1
while counter <10:
    sum = sum + counter
    print(f"The counter,{counter}, and the sum of the counter with sum {sum}")
    counter=counter+1
'''
#ex3
'''
i = 1
n = int(input("enter the limit"))
while (i <=n) :
    if i%2==0:
        print(f"the even number is {i}")
    else:
        print(f"{i}is odd number")
    i=i+1
    print("DONE")
'''
#ex4
'''
import random
target_number= random.randint(1,9)
number=0
while True :
    user_guess=int(input("enter your guess between 1 and 9:"))
    if user_guess==target_number:
        print("well guessed")
        break
    else:
        print("try again")
        number= number + 1
    print("tried", number)
'''
#ex5
'''
user_input=""
while user_input!="exit":
    user_input=input("type something(or exit to quit):")
    print("you typed:",user_input)
'''
#ex6
'''
import random
flip=random.choice(["head","tail"])
while flip!="head":
    print("flipped:",flip)
'''
#ex7
first=0
while first<=5:
    second=1
    while second<=5:
        print(f"{first}times{second}is {first*second:d}")
        second=second+1
    print("ignored the innor loop")
    first=first+1
    print('all done')
#ex8
i = 1
while i<=5:
    print(i)
    i=i+1
for i in range (5):
    print(i)


