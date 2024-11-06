# a=8
# b=3
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# x=5
# x=x+3
# print(x)
# a=True
# b=False
# print(a, b)
# print(type(a),type(b)
x=10
if x>5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
a=15
b=10
if a+b >20:
    print("sum is greater than 20")
else:
     print("sum is less than or equal to 20")
num=7
if num>5:
    if num<10:
        print("Number is between 5 and 10")

maths_marks=int(input("enter maths marks"))
physics_marks=int(input("enter physics marks"))
chemistry_marks=int(input("enter chemistry marks"))
percentage=int(((maths_marks+physics_marks+chemistry_marks)/300)*100)
print("percentage:",percentage)
if percentage>=35:
    print("pass")
else:
    print("fail")
if percentage>=35:
    print("you get a mobile")
    if percentage>=50:
        print("you get a laptop")
        if percentage>=76:
            print("you get a bike")
            if percentage>90:
                print("you get a car")
else:
    print("no gift")