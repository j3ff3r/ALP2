def echtTeiler(n):
	result=[]
	for i in range(1,n):
		if n%i==0:
			result.append(i)
	return result

def listSum(x):
	result=0
	for i in x:
		result+=i
	return result

def friends(a,b):
	if listSum(echtTeiler(a)) == b and listSum(echtTeiler(b)) == a:
		return True
	else:
		return False

def test(y):
	xtest1=9363584
	xtest2=9437056
	y=friends(xtest1,xtest2)
	return y

y=True
y=test(y)
print(y)
