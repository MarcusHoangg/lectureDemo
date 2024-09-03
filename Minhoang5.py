#Lists
'''
names = ["long", "Minh","Hoang","suman","mark"]
print(names[0])
names[-3]
print(names[-3])
names[3]= Quang
print(names[3])
'''
#
'''
names=[]
name=input("Enter your first name or quit by pressing enter: ")
while name != "":
    names.append(name)
    name=input("Enter your first name or quit by pressing enter: ")
print(name)
for n in names:
      print(f"Hello,{n}!")

#some common list operations
'''
'''
names=["a","b","c","d","e","f","g","h"]
names.remove("c")
print(names)
names.insert(0,"x")
print(names)
otherNames = ["m","k"]
names.extend(otherNames)
print(names)
what_index=names.index("a")
print(what_index)
if "k"in names:
    print("found")
names.sort()
print(names)
'''
# range
'''
for number in range (3,31,3):
    print(number)
'''
#
'''
num = int(input("Enter a number: "))
for x in range(1,13):
    multiply = x*num
    print("the answer is",multiply)
'''
num = int(input("Enter a number: "))
for x in range(1,num) :
    if x % 2 == 0 :
     print(x,"is even number")
    else:
     print(x,"this is odd number")










