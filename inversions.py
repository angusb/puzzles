# Inversions can be used to detect how similar two lists are (Kendall's 
#rank correlcation). This is applicable with search engine testing. Futhermore, 
# inversions can be used to match a user's preferences with those of others.
# 
# Given a list L = x_1, x_2, ..., x_N of distinct integers between 1 and n
# an inversion is defined as any pair (i,j) where 1 <= i < j <= n such that x_i > x_j
#
# In a list of n numbers there are up to O(n^2) possible inversions.

def merge_and_count(a, b):
	count = 0
	a_i, b_j = 0, 0
	merge_list = []

	while a_i < len(a) and b_j < len(b):
		merge_list.append(min(a[a_i], b[b_j]))
		if b[b_j] < a[a_i]:
			count += len(a) - a_i

		if a[a_i] <= b[b_j]:
			a_i += 1
		else:
			b_j += 1

	if a_i < len(a):
		merge_list.extend(a[a_i:])
	elif b_j < len(b):
		merge_list.extend(b[b_j:])

	return count, merge_list

def sort_and_count(l):
	if len(l) <= 1:
		return 0, l

	mid = len(l)/2
	a = l[:mid]
	b = l[mid:]

	c_a, a = sort_and_count(a)
	c_b, b = sort_and_count(b)
	c, L = merge_and_count(a, b)

	return c_a + c_b + c, L

def inversions(l):
	return sort_and_count(l)[0]

if __name__ == '__main__':
	assert inversions([1, 3, 0, 2, 4]) == 3
