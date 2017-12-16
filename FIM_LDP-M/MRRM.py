"""Randomized Response Mechanism"""
__author__ = 'DWADE'

from random import SystemRandom
import random
import numpy as np
import math
"""

"""

class MRRM:

    #eplison=0  #the privacy budget
    #p=0        #the first probability
    eplison1=0  #privacy budget 1
    eplison2 = 0  # privacy budget 2
    pb_vector=[] # the vector of privacy budget
    item_k=[]   #the vector of item-category
    def __init__(self,data,eplison1,eplison2,pb_vector,item_k):
        self.eplison1=eplison1
        self.eplison2 = eplison2
        self.pb_vector=pb_vector
        self.data=data
        self.item_k=item_k
        self.len_data=len(data)
        self.result=np.zeros(self.len_data,dtype=np.int16)
    def randomer(self):
        i=0
        t=0
        for k in self.item_k:
            if self.pb_vector[i]==0:
                for j in range(0,k):
                    self.result[t]=self.data[t]
                    t=t+1
            elif self.pb_vector[i]==1:
                for j in range(0,k):
                    rand = SystemRandom()
                    probability = rand.random()
                    bit = probability <math.exp(self.eplison1/2)/(1+math.exp(self.eplison1/2))
                    if bit==1:
                        self.result[t]=self.data[t]
                    else:
                        self.result[t] = 1-self.data[t]
                    t=t+1
            elif self.pb_vector[i]==2:
                vector_t=[]
                for tmp in range(t,t+k):
                    if self.data[tmp]==1:
                        j=tmp
                    else:
                        vector_t.append(tmp)
                rand = SystemRandom()
                probability = rand.random()
                bit = probability < math.exp(self.eplison2) / (k-1 + math.exp(self.eplison2))
                if bit==1:
                    j=j
                else:
                    tmp1=random.randint(0,k-2)
                    j=vector_t[tmp1]
                self.result[j]=1
                t=t+k
            i=i+1
        return self.result



