def myPattern():
	no1 = int(input("Please enter number"));
	for i in range(0,no1):
		for j in range(0,no1):
			print("*", end=" ");
		print("\r")
myPattern();