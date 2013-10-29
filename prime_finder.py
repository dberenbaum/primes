#Simple methods to find prime numbers
from math import *

def prime_finder(n):
#Determine whether a number is prime.
	
    #Check whether proper input type
	if type(n) != int:
		return 'input must be an integer'
	if n < 2:
		return 'input must be greater than or equal to 2'
		
    #Make initial list of possible divisors from 2 to the square root of n
    #Note that a number greater than the square root of n must be multiplied by a number less than the square root of n to get the product n
	max_divisor = int(sqrt(n))
	divisors = list(range(2,max_divisor+1))
	
    #Check if the minimum number in the list is a divisor of n, and if so, return "not prime"
    #If not a divisor of n, remove every factor of that divisor from the list and repeat
    #Note that if n is indivisible by that number, n will also be indivisible by every factor of that number
	while len(divisors) > 0:
		first = divisors[0]
		if n%first == 0:
			return 'not prime'
		divisors = [e for e in divisors if e%first != 0]
	
    #If divisor list emptied without returning "not prime," n is prime
	return 'prime'

def primes_to_n(n):
#Return all primes less than or equal to n.
	
    #Check whether proper input type
	if type(n) != int:
		return 'input must be an integer'
	if n < 2:
		return 'input must be greater than or equal to 2'
	
    #Make a list of all integers from 2 to n and an empty list to store prime numbers
	nums = list(range(2,n+1))
	primes = []
	
    #Cycle through the list by taking the first (minimum) number in it and removing every factor of it from the list
    #After each cycle, the first (minimum) number remaining is prime because it is not a factor of (i.e. is not divisible by) any lower integer
	while len(nums) > 0:
		first = nums[0]
		primes.append(first)
		nums = [e for e in nums if e%first != 0]
	
	return primes
