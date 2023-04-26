num1=int(input("enter a value of num1:"))
num2=int(input("enter a value of num2:"))
operator=(input("enter the operator...(+,-,*,/)"))
if operator=="+":
    print("the sum is",+ num1+num2)
elif operator=="-":
    print("the sub is",+ num1-num2)
elif operator=="*":
    print("the mul is",+ num1*num2)
elif operator=="/":
    print("the ratio is",+ num1/num2)
else:
    print("invalid operator")
   

