#geometryczne.py
def test():
	print("geometryczne")
	return 0

def nth(a1,q,n):
	return a1*q**(n-1)

def sum(a1,q,n):
	if q!=1:
		return a1*((1-q**n)/(1-q))
	else:
		return a1*n

















