a = [2,4,10,16]
multiplier=2
def multiply(arr, multiplier):
	for i in range(len(arr)): 
		arr[i] = arr[i] * multiplier
	return arr
multiply(a, multiplier)
print a
 	
b = multiply(a,5)
print b