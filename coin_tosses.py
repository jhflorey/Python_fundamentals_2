# Create a program that simulates throwing a coin 5,000 times.
# Your program should display how many times the head/tails appears

import random
import math

print 'Starting the program...'

head_count = 0
tail_count = 0
for i in range (1, 5001):
	rand = round(random.random())
	if rand == 0:
		face = 'tail'
		tail_count += 1
	else:
		face = 'head'
		head_count += 1
	print "Attemp #" +str(i)+": Throwing a coin...It's a "+face+"!...Got "+str(head_count)+" head(s) so far and "+str(tail_count)+" tail(s) so far"

print 'Ending the program, thank you!'