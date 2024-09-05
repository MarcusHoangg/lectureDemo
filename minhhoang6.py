from wsgiref.util import request_uri
'''
print("hello")
def greetings():
    print("hello metroplia")
greetings()
a=5
b=6
sum=a+b
print(f"{sum}",greetings())
greetings()
def multiply()
    return n*n
print(f'printting a return function',multiply())
cal=multiply()+10
print(f"the actual vakue {multiply()},increased by 10")
'''
#assignment
'''
def addMe(a,b):
    total=a+b
    print(f"the total : {total}")
#another way
def addMe(a,b):
    total=a+b
    return total
print(f"the sum is {addMe(4,5)}")

def addMe(a,b):
    total=a+b
    return total
total=134
print(f"the sum is {addMe(4,5)}")
print(f"total {total} outside of a function")
print(f"total inside the {addMe(4,5)}")
print(f'total {total} outside of a function')
'''
'''
def multiply(a,b):
    total=a*b
    return total
    print(f"the total:{multiply}")
def divide(a,b):
    if b==0:
        pass
    else:
    total=a/b
    return total

'''
'''
def calTotal(amount,discount=2):
    discountValue = amount*discount/100
    return amount-discountValue
amount=int(input("enter amount:"))
total=calTotal(amount,discount=2)
print(f"total {total}")
'''
'''
score=[]
def square(number):
    return number*number
while True:
    n=int(input("enter a number:"))
    if n ==0:
        break
    else:
        score.append(n)
    print(f"{n} square",square(n))
    print("here is the list")
    print(score)
    for i in score:
       print(f"square of {i}: {square(i)}")
'''
#exercise1
'''
def calculate_sum(numbers):
    total=0
    for number in numbers:
        total+=numbers
    return total
 '''
#ex2
'''
def find_largest(numbers):
    for number in numbers:
        if number>largest:
            largest=number
            return largest
#ex3
def find_smallest(numbers):
    smallest=numbers[0]
    for number in numbers:
        if number<smallest:
            smallest=number
            return smallest
'''
#ex4






