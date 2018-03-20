name=input("please enter your name:")
age= input("please enter your age:")
print('My name is ',name, ' and my age is ', age)

first_name=input("Please enter your first name:")
last_name=input("Please enter your last name:")
full_name=first_name+" "+last_name
print('Hello, my name is {} and my age is {}'.format(full_name,age))


#Afternoon class

def print_lyrics():
    print("Hey Jude, don't make it bad.")
    print("Take a sad song and make it better.")
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print('Na- na- na- na- na- na- na- na- na- na\n'*5)
    print_lyrics()

repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice("Amy")

def give_a_break():
    s='break'
    return s

print(give_a_break())
print_twice(give_a_break())

def cal(a,b):
    return a + b
print(cal(1,2))

def my_abs(n):
    if n>=0:
        return n
    else:
        return -n

print("The absolute value is ", my_abs(-8), ".")


import math
def quadratic(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant >=0:
        x1= (-b + math.sqrt(discriminant))/(2*a)
        x2= (-b - math.sqrt(discriminant))/(2*a)
        return x1 , x2
    else:
        return None, None

input_a=float(input("Please enter a:"))
input_b=float(input("Please enter b:"))
input_c=float(input("Please enter c:"))

sol_1,sol_2=quadratic(input_a,input_b,input_c)
if sol_1:
    print('Results are: {} and {}'.format(sol_1,sol_2))
else:
    print("no solution.")


age=int(input("Enter your age"))

if age <=6:
    print("kid")
elif age>=18:
    print("Adult")
else:
    print("teenager")


def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
print(fib(5))


