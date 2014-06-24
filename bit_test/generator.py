import random
import os
import HTML
import re
from xhtml2pdf import pisa 
import subprocess

def test_q_1(x):
	orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
	insert = random.choice([10, 11, 12 ,13 ,14 ,15])
	number = random.choice([5,6,7,8])
	a = orig|(insert<<number)

	z = open(str(x)+"_test.txt","a")
	z.write(('a = ?      ..........\n'))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number),")\n\n")))

	z = open(str(x)+"_test_answers.txt","a")
	z.write(''.join(('a = ?      ',("0x%X")%a,'\n')))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number),")\n\n")))

def test_q_2(x):
	orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
	insert = random.choice([10, 11, 12 ,13 ,14 ,15])
	number = random.choice([5,6,7,8])
	a = orig|(insert<<number)

	z = open(str(x)+"_test.txt","a")
	z.write(('a = ?      ..........\n'))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number),")\n\n")))

	z = open(str(x)+"_test_answers.txt","a")
	z.write(''.join(('a = ?      ',("0x%X")%a,'\n')))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number),")\n\n")))

def test_q_3(x):
	orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
	insert = random.choice([10, 11, 12 ,13 ,14 ,15])
	number1 = random.choice([7,8]) 	
	if number1 == 7:
 		number2 = 5 
	elif number1 == 8:
		number2 = 6

	a = orig|(insert<<number1)
	b = orig|(insert<<number2)
	answer = (a&b)

	z = open(str(x)+"_test.txt","a")
	z.write(('AND = ?      ..........\n'))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number1),")\n")))
	z.write(''.join(('int b = orig|(insert << ',str(number2),")\n")))
	z.write(('int AND = a&b\n\n'))

	z = open(str(x)+"_test_answers.txt","a")
	z.write(''.join(('AND = ?      ',("0x%X")%answer,'\n')))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number1),")\n")))
	z.write(''.join(('int b = orig|(insert << ',str(number2),")\n")))
	z.write(('int AND = a&b\n\n'))

def test_q_4(x):
	orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
	insert = random.choice([10, 11, 12 ,13 ,14 ,15])
	number1 = random.choice([7,8]) 	
	if number1 == 7:
 		number2 = 5 
	elif number1 == 8:
		number2 = 6

	a = orig|(insert<<number1)
	b = orig|(insert<<number2)
	answer = (a&b)

	z = open(str(x)+"_test.txt","a")
	z.write(('AND = ?      ..........\n'))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number1),")\n")))
	z.write(''.join(('int b = orig|(insert << ',str(number2),")\n")))
	z.write(('int AND = a&b\n\n'))

	z = open(str(x)+"_test_answers.txt","a")
	z.write(''.join(('AND = ?      ',("0x%X")%answer,'\n')))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig|(insert << ',str(number1),")\n")))
	z.write(''.join(('int b = orig|(insert << ',str(number2),")\n")))
	z.write(('int AND = a&b\n\n'))

def test_q_5(x):
	orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
	insert = random.choice([10, 11, 12 ,13 ,14 ,15])
	number_1 = random.choice([7,8])
	if number_1 == 7:
		number_2 = 5 
	elif number_1 == 8:
		number_2 = 6
	a = orig|(insert<<number_1)
	b = orig|(insert<<number_2)
	answer = a^b;

	z = open(str(x)+"_test.txt", "a")
	z.write('OR = ?      ..........\n')
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig | ( insert << ',str(number_1),')\n')))
	z.write(''.join(('int b = orig | ( insert << ',str(number_2),')\n')))
	z.write(''.join('int XOR = a^b\n\n'))

	z = open(str(x)+"_test_answers.txt", "a")
	z.write(''.join(('OR = ?      ',("0x%X")%answer,"\n")))
	z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
	z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
	z.write(''.join(('int a = orig | ( insert << ',str(number_1),')\n')))
	z.write(''.join(('int b = orig | ( insert << ',str(number_2),')\n')))
	z.write(''.join('int XOR = a^b\n\n'))

def test_q_6(x):
	i = random.choice([41120,45232,49344,53456,57568,61680])
	chislo = (random.randint(3,10))
	answer = (i|(1 << chislo))
	z = open(str(x)+"_test.txt", "a")
	z.write('left = ?      ..........\n')
	z.write(''.join(('int i = ',("0x%X")%i,"\n")))
	z.write(''.join(('int left = ',("0x%X")%i," |(1 << ",str(chislo),");","\n\n")))

	z = open(str(x)+"_test_answers.txt", "a")
	z.write(''.join(('left = ?      ',("0x%X")%answer,"\n")))
	z.write(''.join(('int i = ',("0x%X")%i,"\n")))
	z.write(''.join(('int left = ',("0x%X")%i," |(1 << ",str(chislo),");","\n\n")))

def test_q_7(x):
	value1 = random.choice([10*285217024,11*285217024,12*285217024,13*285217024,14*285217024,15*285217024])
	value2 = random.choice([10*268505089,11*268505089,12*268505089,13*268505089,14*268505089,15*268505089])
	result = (value1 << 3) ^ (value2 >> 2)
        
	z = open(str(x)+"_test.txt", "a")
	z.write('result = ?      ..........\n')
	z.write(''.join(('long value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('long value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 3) ^ (value2 >> 2)\n\n")))

	z = open(str(x)+"_test_answers.txt", "a")
	z.write(''.join(("result = ?      ",("0x%X")%result,'\n')))
	z.write(''.join(('long value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('long value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 3) ^ (value2 >> 2)\n\n")))

def test_q_8(x):
	value1 = random.randint(128,1024)
	number = random.uniform(3.0,4.0)
	value2 = value1*number
	value2 = (int(value2))
	result = ((value1 << 3) ^ (value2 >> 2))
        
	z = open(str(x)+"_test.txt", "a")
	z.write('result = ?      ..........\n')
	z.write(''.join(('int value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('int value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 3) ^ (value2 >> 2)\n\n")))
        
	z = open(str(x)+"_test_answers.txt", "a")
	z.write(''.join(("result = ?      ",("0x%X")%result,'\n')))
	z.write(''.join(('int value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('int value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 3) ^ (value2 >> 2)\n\n")))

def test_q_11(x):
	value1 = random.randint(128,1024)
	number = random.uniform(3.0,4.0)
	value2 = value1*number
	value2 = (int(value2))
	result = ((value1 << 3) ^ (value2 >> 2))
        
	z = open(str(x)+"_test.txt", "a")
	z.write('result = ?      ..........\n')
	z.write(''.join(('int value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('int value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 3) ^ (value2 >> 2)\n\n")))
        
	z = open(str(x)+"_test_answers.txt", "a")
	z.write(''.join(("result = ?      ",("0x%X")%result,'\n')))
	z.write(''.join(('int value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('int value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 3) ^ (value2 >> 2)\n\n")))

def test_q_12(x):
	value1 = random.randint(256,1024)
	number = random.uniform(7.0,10.0)
	value2 = int(value1*number)
	result = ((value1 << 5) ^ (value2 >> 4))
        
	z = open(str(x)+"_test.txt", "a")
	z.write('result = ?      ..........\n')
	z.write(''.join(('int value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('int value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 5) ^ (value2 >> 4)\n\n")))
        
	z = open(str(x)+"_test_answers.txt", "a")
	z.write(''.join(("result = ?      ",("0x%X")%result,'\n')))
	z.write(''.join(('int value1 = ',("0x%X")%value1,"\n")))
	z.write(''.join(('int value2 = ',("0x%X")%value2,"\n")))
	z.write(''.join(("int result = (value1 << 5) ^ (value2 >> 4)\n\n")))



print 'Enter the amount of tests you require...'
n = raw_input()
n = int(n)

for x in xrange(1,n+1):
	test_q_1(x)
	test_q_2(x)
	test_q_3(x)
	test_q_4(x)
	test_q_5(x)
	test_q_6(x)
	test_q_7(x)
	test_q_8(x)
	test_q_11(x)
	test_q_12(x)
	test_q_5(x)
	test_q_6(x)

for x in xrange(1,n+1):
	with open(str(x)+"_test.txt", "r") as task:
   		task = task.read()
   		task = task.split('\n\n')
    	task = [w.replace('\n', '<br />') for w in task]

	table_data = [
        [task[0],task[1]],
        [task[2],task[3]],
        [task[4],task[5]],
        [task[6],task[7]],
        [task[8],task[9]],
        [task[10],task[11]],
    ]

	f = open(str(x)+"_test.html","w")
	htmlcode = HTML.table(table_data)
	f.write("<center><h1>Bitwise operations</br>Variant {v}</h1></center></br>".format(v=id))
	f.write(htmlcode)

for x in xrange(1,n+1):
	with open(str(x)+"_test_answers.txt", "r") as task:
   		task = task.read()
   		task = task.split('\n\n')
    	task = [w.replace('\n', '<br />') for w in task]

	table_data = [
        [task[0],task[1]],
        [task[2],task[3]],
        [task[4],task[5]],
        [task[6],task[7]],
        [task[8],task[9]],
        [task[10],task[11]],
    ]
	f = open(str(x)+"_test_answers.html","w")
	htmlcode = HTML.table(table_data)
	f.write("<center><h1>Bitwise operations</br>Variant {v}</h1></center></br>".format(v=id))
	f.write(htmlcode)

for x in xrange(1,n+1):
	p = subprocess.Popen("pisa "+str(x)+"_test_answers.html", shell=True, stdout=subprocess.PIPE)
	p.wait()
	p = subprocess.Popen("pisa "+str(x)+"_test.html", shell=True, stdout=subprocess.PIPE)
	p.wait()
	os.remove(str(x)+"_test.txt")
	os.remove(str(x)+"_test_answers.txt")
