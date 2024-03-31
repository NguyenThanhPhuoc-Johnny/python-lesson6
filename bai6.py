num = input("Enter a number: ")

if num == int(num):
	for i in range(1,num,1):
		print(num)

ans = str(input("When is python invented? A. 1991, B.1989, C.1000, D.1995: "))
if ans == 'A':
	print("correct")
	ans1 = str(input("Who invented python? A. Guido van Rossum, B. Dennis Ritchie, C. James Gosling, D. Bjarne Strousturp: "))
	if ans1 == 'A':
		print("correct")
        	ans2 = str(input("Which statement in python is used to output something onto the screen? A. print(), B. Count >>, C. def(), D. input() "))
		if ans2 == 'A':
			print("correct")
		else: 
			print("wrong")
	else:
		print("wrong")
		break

else:
	print("wrong")
	break

pass = input("Enter password: ")
B = True
while B:
	if pass == "python":
		print("hello")
		B = False

