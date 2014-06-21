import random

orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
insert = random.choice([10, 11, 12 ,13 ,14 ,15])
number_1 = random.choice([7,8])

if number_1 == 7:
	number_2 = 5 
elif number_1 == 8:
	number_2 = 6

a = (orig|(insert<<number_1))
b = (orig|(insert<<number_2))

answer = (a&b);
print (number_1)
print (number_2)
print (("0x%X")%orig)
print (("0x000%X")%insert)
print (("0x%X")%a)
print (("0x%X")%b)
print (("0x%X")%answer)
