# s=0
# for i in range(1,101):
#     print("s=", s, " i=", i)
#     s=s+i
#     print(s,"\n")

#sum of odd numbers:
# s=0
# for i in range(1,1001):
#     if i % 2 != 0:
#         print('s=', s, ' i= ', i)
#         s=s+i
#
# print(s)


#While:
# from time import sleep
# def countdown(n):
#     while n>0:
#         print(n)
#         n=n-1
#         sleep(1)
#     print('Blastoff!')
#
# countdown(10)

# s=0
# i=1
#
# while i<101:
#     s=s+i
#     i=i+1
#
# print(s)


def sum_integer(n):
    i=1
    s=0
    while i<=n:
        s=s+i
        i=i+1
    return s

print(sum_integer(100))

letter='j'

while True:
    line = input('>')
    if line=="j":
        break
    print(line)
print("Done!")
