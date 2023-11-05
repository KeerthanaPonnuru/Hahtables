import random
from functools import reduce

class Cuckoo:
    
    def __init__(self, entries, k, cuckoo_steps):
        
        
        self.cuckoo_steps = cuckoo_steps
        self.entries = entries
        self.k = k
        self.T = [[0, 0] for i in range(self.entries)]

        
    def hash(self):
    	self.s = random.sample(range(0, 10000000000000), self.k)

    def insert(self, fid):
        
        i=0
        while(i<len(self.s)):

        	l=[fid,self.s[i]]
        	res=reduce(lambda x,y: x^y,l)
        	ind = res % self.entries
        	x=self.T[ind][0]
        	y=self.T[ind][1]
        	if x == 0:
        		self.T[ind][0] = fid
        		y += 1
        		return
        	else:
        		y += 1
        		i=i+1
        j=0
        while(j<self.k):
            ind = (fid ^ self.s[j]) % self.entries
            id = x
            if (not self.move(id, self.cuckoo_steps)):
            	pass
            else:
                x = fid
                y += 1
                return
            j=j+1


    def move(self, id, cuckoo_steps):
     
        if cuckoo_steps == 0:
            return False
        i=0
        while(i<self.k):
            ind = (id ^ self.s[i]) % self.entries

            if self.T[ind][0] == id or self.T[ind][0] != 0:
            	pass

            else:
                self.T[ind][0] = id
                return True
            i=i+1

        j=0
        while(j<self.k):
            if self.T[ind][0] == id or not self.move(id, cuckoo_steps - 1):
            	pass
            else:
                self.T[ind][0] = id
                return True
            j=j+1
        return False


if __name__ == "__main__":

    i, j, z, c=0, 0, 0, 0 
    entries = int(input("table entries: "))
    number_of_flows = int(input("flows: "))
    k = int(input("hashes: "))
    cuckoo_steps = int(input("cuckoo steps: "))

    HT = Cuckoo(entries, k, cuckoo_steps)
    flows = random.sample(range(0, 10000000000000), number_of_flows)
    HT.hash()
    while(i<entries):
        HT.insert(flows[i])
        i=i+1

    file = open('cuckoo.txt', 'w')
   
    while(j<entries):
        if HT.T[j][0] == 0:
        	pass
        else:
            c += 1
        j=j+1

    
    print(c, file=file)
    

    while(z<entries):
        
        print(str(HT.T[z][0]), file=file)
        z=z+1



