def myfact():
	no1 = int(input("Please enter number"));
	fact = 1
	for i in range(1,no1+1):
		fact = fact * i;
	print("The factorial is = : ", end=" ")
	print (fact)
myfact();