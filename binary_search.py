
class Binary_Search:

	def iterative(self,A,t):
		n = len(A)
		p = 0
		r = n - 1
		while p <= r:
			m = int((p + r)/2)
			if t < A[m]:
				r = m -1
			if t > A[m]:
				p = m + 1
			if t == A[m]:
				return m
		return -1

	def recursive(self,A,t,p,r):
		if p > r:
			return -1
		m = int((p + r)/2)
		if t < A[m]:
			r = m - 1
			i = self.recursive(A,t,p,r)
		if t > A[m]:
			p = m + 1
			i = self.recursive(A,t,p,r)
		if t == A[m]:
			return m
		return i
