x=int(input("Enter first range number: "))
y=int(input("Enter last range number: "))

l1=[i for i in range(x,y) if i%2 ==0]
l2=[i for i in range(x,y) if i%2 !=0]

print(f"Even numbers are: {l1}")
print(f"Odd numbers are: {l2}")


fruits=["grape","pineapple","cherry","papaya","peach","fig","coconut","plum","apricot","watermelon"]

fCap=[i.capitalize() for i in fruits]
print(fCap)
