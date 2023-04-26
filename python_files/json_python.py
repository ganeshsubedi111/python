# json in python
''''
javascript object notation
used for storing and transfering data betwn the browser and server
it is a text written with javascript  object notation

import json
'''
import json
d={
    "coursename":"python",
   " fees": 2000
}
f=json.dumps(d)
print(type(f))
print(f)