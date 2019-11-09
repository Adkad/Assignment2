def myAdd():
	no1 = int(input("Please enter number :"));
	tot = 0;
	while(no1 >0):
		tot = tot + no1 % 10;
		no1 = int(no1/10);
	print("Output : ",tot);
myAdd();