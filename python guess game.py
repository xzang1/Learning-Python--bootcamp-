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
        if int(input_number)<random_number and int(input_number)<1000 and int(input_number)>0:
            trial-=1
            print("your number is too low",", and you have %d times left"%trial)
        elif int(input_number)>random_number and int(input_number)<1000 and int(input_number)>0:
            trial-=1
            print("your number is too high",", and you have %d times left"%trial)
        elif int(input_number)>1000 or int(input_number)<0:
            print("Please enter a number within the range of 0 to 1000")
        else:
            print("Good job ",input_name," ! You did it!")
            break
    else:
        print("You broke the game!")
print("Too bad, you ran out of 6 guesses",". The output is %d"%random_number)
