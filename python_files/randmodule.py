#Random module in python -random module means - already built in module

# random.randint() method
import random
print(random.randint(15,25))
# random.randrange() method
print(random.randrange(10,16))
# random.choice() method
l=[20,10,45,35,65]
print(random.choice(l))

# random()
print(random.random())# return random number between 0 and 1

#shuffle()
random.shuffle(l)
print(l)

#uniform()
u=random.uniform(10,16)# return float
print(u)