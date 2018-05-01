

def echtTeiler(n):
	result=[]
	for i in range(1,n):
		if n%i==0:
			result.append(i)
	return result


def test(y):
	xtest=10988
	y=echtTeiler(xtest)
	return y

y=[]
y=test(y)
print(y)
