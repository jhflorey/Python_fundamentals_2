def scores_and_grades():
	print 'scores_and_grades'
	for score in range (60,100):
		if score >= 90:
			print 'Score:', score ,'; Your grade is A'
		elif score >= 80 and score < 90:
			print 'Score:', score ,'; Your grade is B'
		elif score >= 70 and score < 80:
			print 'Score:', score ,'; Your grade is C'
		else:
			print 'Score:', score ,'; Your grade is D'
	return

scores_and_grades()
print "End of program. Bye!"