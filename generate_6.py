import random

i = random.choice([41120,45232,49344,53456,57568,61680])
chislo = (random.randint(3,10))
left = (i|(1 << chislo))
print("0x%X"%i)
print("0x%X"%left)
