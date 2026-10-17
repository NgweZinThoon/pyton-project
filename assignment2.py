x=int(input("Give me a first number:"))
y=int(input("Give me a second number:"))
z=input("Choice your operator(+,-,*,/):")


def add(x,y):
    print(x+y)
    
def sub(x,y):
    if x > y :
        print(x-y)
    elif y > x :
        print(y-x)
    
def multi(x,y):
    print(x*y)
    
def div(x,y):
    if x > y :
        print(x/y)
    elif y > x :
        print(y/x)
    
if z=="+":
    add(x,y)
    
elif z=="-":
    sub(x,y)
    
elif z=="*":
    multi(x, y)
    
elif z=="/":
    div(x, y)

    