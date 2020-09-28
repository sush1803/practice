#pyramid pattern
 #      0 1 2 3 4 5    i=0 i=1 i=2   n=  num of space=1  6 rows
 #      0 1 2 3 4                        num of star=2   6 clmn
#       0 1 2 3
#       0 1 2
#       0 1
#       0
###########
#       0                       i=0  0
# 2 4
# 6 8 10
# 12 14 16 18
# 20 22 24 26 28
#       0
#       2 4
#       6 8 10
#       12 14 16 18
n=int(input("enter row number:")) #n=4
num=0
for row in range(0,n+1):
    for col in range(0,row+1):
        if num%2==0:
            print(num, end=' ')
            num=num+2
    print()

