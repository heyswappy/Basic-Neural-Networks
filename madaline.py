from adaline import Adaline

class Madaline:
    def __init__(self, n, hid, rate=0.3, thresh=1.2):
        self.count = n+1;
        self.hid_count = hid+1
        self.rate = rate
        self.thresh = thresh
        self.units = [Adaline(n, rate, thresh) for i in range(hid)]
        self.edges = [1]*(hid+1)
        return
    
    def activation(self, x):
        if x > self.thresh:
            return 1
        else:
            return -1
    
    def fit(self, s, z, info=False):
        # s is vector of training inputs
        # z is a vector of outputs
        # for each training pair
        flag = True
        while(flag):
            flag = False
            for i in range(len(s)):
                result = [1]
                result += [j.predict(s[i]) for j in self.units]
                print(list(self.edges[j]*k for j, k in enumerate(result)))
                result_sum = sum(self.edges[j]*k for j, k in enumerate(result))
                to_update = []
                # mark hidden nodes to update
                for j in range(len(self.edges)):
                    alternative = 1 if result[j] == -1 else -1
                    new_activation = self.activation(result_sum - result[j] + alternative)
                    new_z = self.activation(new_activation)
                    if new_z == self.predict(s[i]):
                        to_update.append(j)
                    else:
                        print("correct")
                print("UPDATE",to_update)
                # update the marked nodes
                for j in to_update:
                    flag = True
                    if j == 0:
                        self.edges[0] += z[i]*self.rate
                    else:
                        self.units[j-1].fit([s[i]],[z[i]])

        if not info:
            return
        print("Training Complete")
        for i in range(len(s)):
            out = self.predict(s[i])
            print("Output is: ",out," should be: ",z[i])
        return

    def predict(self, s):
        result = [self.edges[0]]
        result += [j.predict(s)*self.edges[i+1] for i, j in enumerate(self.units)]
        result = self.activation(sum(result))
        return result

if __name__ == "__main__":
    n = int(input("The number of neurons:"))
    h = int(input("The number of hidden neurons:"))
    t = int(input("The number of inputs(training_data_count):"))
    s = [list(map(int,input("Input? :").strip(" ").split(" "))) for i in range(t)]
    z = [int(input("Output? :")) for i in range(t)]
    net = Madaline(n, h, 0.2, 0.5)
    net.fit(s, z, True)
    for i in s:
        print(net.predict(i))
