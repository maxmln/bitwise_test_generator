import random
value1 = random.randint(256,4096)
number = random.uniform(3.0,4.0)
value2 = int(value1*number)

result = (value1 << 3) | (value2 >> 2)

print value1
print value2
print (("0x%X")%result)
