class Hebb:
	def __init__(self, n, rate=1, thresh=1):
		self.count = n+1
		self.rate = rate
		self.thresh = thresh
		self.edges = [0]*(n+1)
	
	def activation(self, x):
		if x > self.thresh:
			return 1
		else:
			return -1

	def _update(self, s, z):
		# s --> input
		# z --> output
		self.edges[0] += 1*z*self.rate
		for i in range(1, self.count):
			self.edges[i] += s[i-1]*z*self.rate
		return

	def fit(self, s, z, info=False):
		# s -->  list of inputs
		# z --> list of corresponding outputs
		# info --> show information or not
		for i in range(len(s)):
			self._update(s[i],z[i])
		if not info :
			return
		
		print("Training Complete")
		for i in range(len(s)):
			out = self.predict(s[i])
			print("Output is: ",out," should be: ",z[i])
		return

	def predict(self, s):
		# s is an input
		ans = self.edges[0]
		for i in range(1,self.count):
			ans += s[i-1]*self.edges[i]
		return self.activation(ans)

if __name__ == "__main__":
	n = int(input("The number of neurons:"))
	t = int(input("The number of inputs(training_data_count):"))
	s = [list(map(int,input("Input? :").strip(" ").split(" "))) for i in range(t)]
	z = [int(input("Output? :")) for i in range(t)]
	net = Hebb(n)
	net.fit(s, z, False)
	for i in s:
		print(net.predict(i))
