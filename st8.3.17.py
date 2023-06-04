from sys import argv

def five(n):
	if n <= 0:
		print(n)
		return True
	print(n)
	n = n - 5
	five(n)
	print(n+5)	

five(int(argv[1]))
