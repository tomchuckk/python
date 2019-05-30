# HW3 - Calculator
# CSE 1010 - Introduction to Computing for Engineers
# Alex Tomczuk
# Yijue Wang, Section 002L
# February 17, 2019

contin = True
accum=float(0)

while contin:
	try:
		print('Accumulator = ', accum)
		print('Please choose one of the following options:')
		print('1) Addition')
		print('2) Subtraction')
		print('3) Multiplication')
		print('4) Division')
		print('5) Square root')
		print('6) Clear')
		print('0) Exit')
		opt=int(input('What is your option? '))
		
		if opt==0:
			contin=False
		elif opt==1:
			numb=float(input('Enter a number here: '))
			accum=accum+numb #add
		elif opt==2:
			numb=float(input('Enter a number here: '))
			accum=accum-numb #subtract
		elif opt==3:
			numb=float(input('Enter a number here: '))
			accum=accum*numb #multiply
		elif opt==4:
			numb=float(input('Enter a number here: '))
			accum=accum/numb #divide
		elif opt==5:
			if accum<0: #check if accumulator is negative
				print('undefined value')
			else:
				accum=accum**(0.5) # square root
		elif opt==6:
			accum=float(0) # clear		
	except:
		print('Please choose a valid option')
