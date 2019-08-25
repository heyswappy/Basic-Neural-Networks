class hebb:
	def __init__(self, n, alpha=1, threshold=0, bias=1):
		self.net = {}
		self.alpha = alpha
		self.threshold = threshold
		self.net[0] = bias
		for i in range(1,n+1):
			self.net[i] = 0
		self.net["z"] = [0]*(n+1)

	def update(self, s, z):
		n = len(s)
		self.net[0] = self.bias
		for i in range(1,n+1):
			self.net[i] = s[i-1]
		for i in range(n+1):
			self.net["z"][i] = self.net["z"][i] + self.alpha*self.net[i]*z
		return

	def train(self, s, z):
		t = len(s)
		
		for i in range(t):
			self.update(s[i],z[i])
	
		print("TRAINING COMPLETE")
		for i in range(t):
			out = self.output(s[i])
			print("Output is: ",out," should be: ",z[i])
		print("Weights are:")
		print(self.net["z"])
		return

	def output(self, s):
		n = len(s)
		ans = 1*self.net["z"][0]
		for i in range(1,n+1):
			ans += s[i-1]*self.net["z"][i]
		threshold = self.threshold
		if ans >= threshold:
			return 1
		return -1

n = int(input("The number of neurons:"))
t = int(input("The number of inputs(training_data_count):"))
s = []
for i in range(t):
	s.append(list(map(int,input("Input? :").strip(" ").split(" "))))
z = []
for i in range(t):
	z.append(int(input("Output? :")))

net = hebb(n)
net.train(s, z)