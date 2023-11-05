import random
from functools import reduce


class Segment:
   
    def __init__(self, seg_entries):
        self.seg_entries = seg_entries
        self.S = [[0, 0] for i in range(self.seg_entries)]


class DLH:
    

    def __init__(self, entries, segments):
        
        self.segments = segments
        self.entries = entries
        self.seg_entries = int(entries / segments)
        self.T = [Segment(self.seg_entries) for i in range(self.segments)]
        

    def hash(self):
       
        self.s = random.sample(range(0, 10000000000000), self.segments)

    def insert(self, fid):
        i=0
        while(i<len(self.s)):

            l=[fid,self.s[i]]
            res = reduce(lambda x, y: x ^ y, l)
            ind = res % self.seg_entries
            
            x=self.T[i].S[ind][0]
            y=self.T[i].S[ind][1]

            if x== 0:  
                self.T[i].S[ind][0]=fid
                x+=1
                return
            else:  
                y += 1
            i=i+1


if __name__ == "__main__":

    i, j, c,m,n,k=0, 0, 0, 0,0,0
    entries = int(input("table entries: "))
    number_of_flows = int(input("no of flows: "))
    segments = int(input("no of segments: "))

    HT = DLH(entries, segments)
    flows = random.sample(range(0, 10000000000000), number_of_flows)
    HT.hash()
    
    while(i<entries):
        HT.insert(flows[i])
        i=i+1 

    file = open('dleft.txt', 'w')
  
    while(m<segments):
        while(n<int(entries/segments)):
            if HT.T[m].S[n][0] != 0:
                c += 1
            n=n+1
        m=m+1
        n=0

    
    print(c, file=file)
    

    while(k<segments):
        while(j<int(entries/segments)):
            
            print(str(HT.T[k].S[j][0]), file=file)
            j=j+1
        k=k+1
        j=0





