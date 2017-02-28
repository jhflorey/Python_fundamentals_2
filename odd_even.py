def odd_even():
	print 'odd_even'
	for num in range (1,2001):
		# print num
		if num % 2 == 0:
			print 'Number is', num ,'.This is an even number'
		else:
			print 'Number is', num , '.This is an odd number'
	return

odd_even()