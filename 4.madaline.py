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
            print(error,self.tolerance)
            print(self.net["z"])
            input("")

        print("TRAINING COMPLETE")
        for i in range(t):
            out = self.output(s[i])
            print("Output is: ",out," should be: ",z[i])
        print("Weights are:")
        print(net.net["z"])
        return

    def y_in(self, s):
        n = len(s)
        ans = 1*self.net["z"][0]
        for i in range(1,n+1):
            ans += s[i-1]*self.net["z"][i]
        return ans

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
    


class madaline:
    def __init__(self, inp, hid, alpha=1, wt=1, fix_wt=1, threshold=0, bias=1, tolerance=0.1):
        self.net = {0:bias}
        self.hid_count = hid
        self.threshold = threshold
        self.tolerance = tolerance
        for i in range(1,hid+1):
            self.net[i]=(adaline(inp,alpha=alpha, wt=wt, threshold=threshold, bias=bias, tolerance=tolerance))
            
        self.net["z"] = [fix_wt]*(hid+1)
        return
    
    def train(self, s, z):
        # s is vector of training inputs
        # z is a vector of outputs
        l = int(self.hid_count)
        error = self.tolerance + 1
        while(error > self.tolerance):
            error = 0
            for i in range(len(s)):
                # for each training input
                y_in = self.net[0]*self.net["z"][0]
                n = int(self.hid_count)
                for j in range(1,n+1):
                    y_in += self.net[j].output(s[i])*self.net["z"][j]
                
                y = 1 if y_in > self.threshold else -1
                error += (z[i] - y_in)**2

                if(y != z[i] and z[i] == 1):
                    # output is 1 and error occured
                    abs_ind = 1
                    abs_val = self.net[1].output(s[i])
                    for j in range(2,self.hid_count+1):
                        hid_out = self.net[j].output(s[i])
                        if abs_val > abs(hid_out):
                            abs_val = hid_out
                            abs_ind = j
                    self.net[abs_ind].update(s[i], z[i])
                elif(y != z[i] and z[i] == -1):
                    for j in range(1,self.hid_count+1):
                        hid_out = self.net[j].output(s[i])
                        if hid_out > 0:
                            self.net[j].update(s[i], z[i])
                else:
                    pass
            error = error/len(s)
        print("TRAINING COMPLETE")
        l = len(s)
        for i in range(l):
            out = self.output(s[i])
            print("Output is: ",out," should be: ",z[i])
        print("Weights are:")
        print(net.net["z"])
        return

    def output(self, s):
        z = self.net[0]*self.net["z"][0]
        n = self.hid_count
        for i in range(1,n+1):
            z += self.net[i].output(s)*self.net["z"][i]
        
        if z > self.threshold:
            return 1
        else:
            return -1


def inputs():
    n = int(input("The number of neurons:"))
    t = int(input("The number of inputs:"))
    s = []
    for i in range(t):
        s.append(list(map(int,input("Input? :").strip(" ").split(" "))))
    z = []
    for i in range(t):
        z.append(int(input("Output? :")))

    net = adaline(n,wt=0.1,tolerance=0.45,alpha=0.1)
    net.train(s,z)

inp = 2
hid = 2
s = [[-1,-1], [1,-1], [-1,1], [1,1]]
z = [-1,1,1,-1]
alpha = 0.5
wt = 0.6
threshold = 0
tolerance = 1.3
net = madaline(inp, hid, alpha=alpha, wt=wt, threshold=threshold, tolerance=tolerance)
net.train(s,z)
print(net.output(s[0]))
print(net.output(s[1]))
print(net.output(s[2]))
print(net.output(s[3]))