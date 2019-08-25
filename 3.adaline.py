import math
class adaline:
	def __init__(self, n, alpha=1, wt=1,threshold=0, bias=1, tolerance=0.1):
		self.net = {}
		self.alpha = alpha
		self.threshold = threshold
		self.tolerance  = tolerance
		self.net[0] = bias
		for i in range(1,n+1):
			self.net[i] = 0
		self.net["z"] = [wt]*(n+1)

	def update(self, s, z):
		n = len(s)
		for i in range(1,n+1):
			self.net[i] = s[i-1]
		
		y_in = self.net[0]*self.net["z"][0]
		for i in range(1,n+1):
			y_in += s[i-1]*self.net["z"][i]
		
		error = (z - y_in)**2
		if error < self.tolerance:
			return error
		delta = z - y_in 
		wt_change = self.alpha*delta
		self.net["z"][0] += wt_change
		for i in range(1, n+1):
			wt_change = self.alpha*self.net[i]*delta
			self.net["z"][i] += wt_change
		return error
	
	def train(self, s, z):
		t = len(s)
		error = self.tolerance + 1
		while(error > self.tolerance):
			error = 0
			for i in range(t):
				error += self.update(s[i],z[i])
			error = error/t

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
		if ans >= threshold:
			return 1
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

net = adaline(n,wt=0.1,tolerance=0.45,alpha=0.1)
net.train(s,z)