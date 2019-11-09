def myPattern():
	no1 = int(input("Please enter number : "));
	for i in range(no1,0,-1):
		print((no1-1)* "" + i * " *");
myPattern();