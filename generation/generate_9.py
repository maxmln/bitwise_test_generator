import random

testValue = random.choice([10*285217024,11*285217024,12*285217024,13*285217024,14*285217024,15*285217024])
a = 0;
if testValue & (1 << 4):
	a = 1
else:
	a = 2

print a
