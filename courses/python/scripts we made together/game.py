n = int(input("Entre un nbr "))

stars = 1
space = n//2
while space>=0:
    print(" "*space + "*"*stars)
    stars = stars + 2
    space = space -1


space = n//2
for x in range(n):
    print(" "*space+"*")