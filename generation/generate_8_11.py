import random

value1 = random.randint(128,1024)
number = random.uniform(3.0,4.0)
value2 = value1*number
value2 = (int(value2))

result = ((value1 << 3) ^ (value2 >> 2))

print (("0x%X")%result)
