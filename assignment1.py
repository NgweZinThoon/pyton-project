x=int(input("Give me first number:"))
y=int(input("Give me second number"))

all_x=id(x)
all_y=id(y)

print("allocation of first number",all_x)
print("allocation of second number",all_y)

hex_x=hex(x)
hex_y=hex(y)

print("hex value of first number",hex_x)
print("hex value of second number",hex_y)

print(x+y)
print(x*y)

if x > y :
    print(x-y)
    print(x%y)
    
    
elif y > x :
    print(y-x)
    print(y%x)
