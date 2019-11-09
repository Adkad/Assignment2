def myPattern():
	no1 = int(input("Please enter number"));
	for i in range(0,no1):
		no1 =1;
		for j in range(i):
			print(no1, end=" ");
			no1 = no1 +1;
		print(no1)
myPattern();