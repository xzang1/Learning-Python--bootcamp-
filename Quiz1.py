"""
Question 1:
Given two int values, return their sum. Unless the two values
are the same, then return double their sum.
"""

def sum_double(a, b):
    if a==b:
        c=(a+b)*2
        print(c)
    else:
        c=a+b
        print(c)


print(sum_double(1,2))
print(sum_double(2,2))


	
# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(sum_double(1, 2))

# print(sum_double(2, 2))




"""
-----------------------------------------------------------------------
Question 2:

In a small town the population is p0 = 1500 at the beginning of a year.
The population regularly increases by 5 percent per year and moreover 100
new inhabitants per year come to live in the town. How many years does
the town need to see its population greater or equal to p = 5000
inhabitants?

Answer: 15 years

Create a function that takes four parameters to return the number of
years needed.
"""
#
def number_of_years(p0, percent, aug, p):
    x=0
    while p0<p:
        p0=p0*(1+percent/100)+aug
        x=x+1
    return x


# # When you've completed your function, uncomment the
# # following lines and run this file to test!
#
print(number_of_years(1500, 5, 100, 5000))
#
# print(number_of_years(1500000, 2.5, 10000, 2000000))



"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).

"""


def sum_squares(n):
    i=0
    sum=0
    for i in range(n+1):
        sum=sum
        square=i**2
        sum=sum+square
        i+=1
    return sum

print(sum_squares(2))
print(sum_squares(3))

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(100))
