
class Binary_Search:

	def iterative(self,A,t):
		#we can initiate our variables
		n = len(A)
		p = 0
		r = n - 1
		#While left index is less than right index
		while p <= r:
			m = int((p + r)/2)
			
			#if target is less than middle element
			if t < A[m]:
				#Adjust right index
				r = m -1

			#if target is greater than middle element		
			if t > A[m]:
				#Adjsut left index
				p = m + 1
			
			#if target is equal to middle element	
			if t == A[m]:
				#return index
				return m
				
		#return -1 as unsuccessful		
		return -1

	def recursive(self,A,t,p,r):
		
		# left index is greater then right index
		# return -1 as unsuccessful
		if p > r:
			return -1

		# middle index
		m = int((p + r)/2)

		#if target is less than middle element
		if t < A[m]:
			#Adjust right index
			r = m - 1
			i = self.recursive(A,t,p,r)

		#if target is greater than middle element	
		if t > A[m]:
			#Adjust left index
			p = m + 1
			i = self.recursive(A,t,p,r)
		
		#if target is equal to middle element
		if t == A[m]:
			#return index
			return m

		#main return
		return i
