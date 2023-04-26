# json to python object
import json
d='{"course":"python","fees":2000}'
x=json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a,x[a])