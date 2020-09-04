import binary_search as b_search


# Given a sorted array,we can use binary search
# to find the index of an element
A = [2,5,7,9,11,13,15,17,19,21]

# Target element we are searching for
t = 17

# Variables p = first element, r = last element
p = 0
r = len(A)-1

# Create class object
b_s = b_search.Binary_Search()

# Calls the iterative function of Binary Search, returns index of 
# element or -1 if not present
index = b_s.iterative(A,t)

# Calls the recursive function of Binary Search, returns index of 
# element or -1 if not present
r_index = b_s.recursive(A,t,p,r)	


print(index)
print(r_index)