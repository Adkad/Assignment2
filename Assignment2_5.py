def myprime():
	no1 = int(input("Please enter number :"));
	if no1 > 1:
		for i in range(2,no1):
			if(no1%i) != 0:
				print("It is prime number");
			break
myprime();