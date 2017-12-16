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
    def __init__(self,data,eplison1):
        self.eplison1=eplison1
        self.data=data
        self.len_data=len(data)
        self.result=np.zeros(self.len_data,dtype=np.int16)
    def randomer(self):
        for i in range(self.len_data):
            rand = SystemRandom()
            probability = rand.random()
            bit = probability < math.exp(self.eplison1 / 2) / (1 + math.exp(self.eplison1 / 2))
            if bit == 1:
                self.result[i] = self.data[i]
            else:
                self.result[i] = 1 - self.data[i]
        return self.result



