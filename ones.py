#ones
while True:
	try:
		n = int(input())
	except EOFError:
		break
	
	x = 1 % n
	c = 1
	while x != 0:
		x = (x * 10 + 1) % n
		c += 1
	print(c)



while True:
	try:
		n=int(input())
	except EOFError:
		break
	
	x=1%n
	c=1
	while x!=0:
		x=(x*10+1)%n
		c=c+1
	print(c)		