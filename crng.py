from random import random
from time import time
lower_limit = input("Please input the lower limit for the Random Number Generator. ")
upper_limit = input("Please input the upper limit for the Random Number Generator. ")
total_num = input("Please input the number of random numbers to be generated. ")
bias_percentage = input ("Please enter the percentage of the biased numbers towards upper limit.")
def time_random():
	return time() - float(str(time()).split('.')[0])

def random_range(min,max):
	return int(time_random() * (max - min) + min)

if __name__ == '__main__':
	counter = 0
	lower_count = 0
	while (counter+lower_count < total_num):
		mid_limit = int((lower_limit+upper_limit)/2)
		total_biased_nums = int(bias_percentage*total_num/100)
		tmp_vr = random_range(lower_limit,upper_limit)
		if (lower_limit <= tmp_vr <= upper_limit):
			random_num = random_range(lower_limit,upper_limit)
		if (random_num > mid_limit):	
			if (counter < total_biased_nums):
				print random_num
				counter = counter + 1
		elif (random_num < mid_limit) and (lower_count < (total_num-total_biased_nums)):
			print random_num
			lower_count = lower_count + 1
