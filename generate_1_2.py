import random

orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
insert = random.choice([10, 11, 12 ,13 ,14 ,15])
number = random.choice([5,6,7,8])

a = orig|(insert<<number)

print ("0x%X")%orig
print ("0x000%X")%insert
print ("0x%X")%a
