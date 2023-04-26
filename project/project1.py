# number guessing using random
import random
computergenerate=random.randrange(1,101)
userinput=int(input("enter your number:"))
if computergenerate<userinput:
    print("computer generate number is:",computergenerate)
    print("your guess is higher than  that of computer")
elif computergenerate>userinput:
    print("computer generate number is:",computergenerate)
    print("your guess is lower than  that of computer")
elif computergenerate==userinput:
    print("computer generate number is:",computergenerate)
    print("both guess are equal")