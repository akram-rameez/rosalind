# Given: Positive integers n<=40 and k<=5.
# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n,k=map(int,raw_input().split())

a,b=1,1

for x in xrange(1,n):
	pass
	a,b=b,k*a+b

print a