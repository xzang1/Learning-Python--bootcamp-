import random

random_number = int(random.randint(1,1001))

print("Hello, What's your name?")
input_name=input('>>>')
print("Hi",input_name)

print("Take a guess")

trial=10
while trial>0:
    input_number=int(input(">>>"))
    if input_number<random_number:
        trial-=1
        print("your number is too low","you have %d times left"%trial)
    elif input_number>random_number:
        trial-=1
        print("too high","you have %d times left"%trial)
    elif input_number==random_number:
        print("Good job ",input_name," !")
        break
    else:
        print("Too bad, you have 0 times left")
        break

