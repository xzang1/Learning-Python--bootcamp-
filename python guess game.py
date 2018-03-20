import random

random_number = int(random.randint(1,1001))

print("Hello, What's your name?")
input_name=input('>>>')
print("Hi",input_name)

print("Take a guess")

trial=6
while trial>0:
    input_number=input(">>>")
    if input_number.isdigit():
        if int(input_number)<random_number:
            trial-=1
            print("your number is too low","you have %d times left"%trial)
        elif int(input_number)>random_number:
            trial-=1
            print("too high","you have %d times left"%trial)
        else:
            print("Good job ",input_name," !")
            break
    else:
        print("You broke the game!")
print("Too bad, you ran out of 6 guesses",". The output is %d"%random_number)
