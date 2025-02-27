even=[i for i in range(1,21) if i%2==0]

print(even)

#====================================

nums=[1,2,3,4,5,6,7,8,9,10]

def sq(n):
    return n*n

square=map(sq,nums)

print(f"The square numbers list is as follows: {list(square)}")

#=====================================

num1=[9,8,7,6,5,4]
num2=[4,5,6,7,8,9]

res=map(lambda x,y: x+y, num1,num2)

print(list(res))