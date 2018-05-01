#objektorientiertes programmieren Assignment 1
#Tutorium  Fabian Halama Fr 12-14
#John Fischer Thomas Sieron
#Aufgabe 1: Produkt einer Liste 



def listProduct(x):			
	result=1
	for i in x:
		result*=i
	return result


def test(y):
	xtest=[10,3,4,6,7]
	return listProduct(xtest)

y=1
y=test(y)
print(y)
