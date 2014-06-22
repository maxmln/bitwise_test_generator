import random

value1 = random.choice([10*285217024,11*285217024,12*285217024,13*285217024,14*285217024,15*285217024])
value2 = random.choice([10*268505089,11*268505089,12*268505089,13*268505089,14*268505089,15*268505089])

result = (value1 << 3) ^ (value2 >> 2)

print hex(value1)
print hex(value2)
print hex(result)
