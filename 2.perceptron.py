class perceptron:
	def __init__(self, n, alpha=1, threshold=1, bias=1):
		self.net = {}
		self.alpha = alpha
		self.threshold = threshold
		self.net[0] = bias
		for i in range(1,n+1):
			self.net[i] = 0
		self.net["z"] = [0]*(n+1)

	def update(self, s, z):
		n = len(s)
		for i in range(1,n+1):
			self.net[i] = s[i-1]
		for i in range(n+1):
			self.net["z"][i] = self.net["z"][i] + self.alpha*self.net[i]*z
		return
	
	def train(self, s, z):
		flag = 0
		t = len(s)

		while(flag != t):
			flag = 0
			for i in range(t):
				out = self.output(s[i])
				if out != z[i]:
					self.update(s[i],z[i])
				else:
					flag += 1
			if flag ==t:
				print("TRAINING COMPLETE")
				for i in range(t):
					out = self.output(s[i])
					print("Output is: ",out," should be: ",z[i])
				print("Weights are:")
				print(net.net["z"])
		return

	def output(self, s):
		n = len(s)
		ans = 1*self.net["z"][0]
		for i in range(1,n+1):
			ans += s[i-1]*self.net["z"][i]
		threshold = self.threshold
		if ans > threshold:
			return 1
		elif -threshold <= ans <= threshold:
			return 0
		else:
			return -1

n = int(input("The number of neurons:"))
t = int(input("The number of inputs(training_data_count):"))
s = []
for i in range(t):
	s.append(list(map(int,input("Input? :").strip(" ").split(" "))))
z = []
for i in range(t):
	z.append(int(input("Output? :")))

net = perceptron(n)
net.train(s,z)