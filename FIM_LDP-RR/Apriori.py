"""Private Apriori Algorithm"""
__author__ = 'DWADE'
import numpy as np
import math

class Apriori:
    data=[]             #数据
    minsup=1            #支持度阈值
    epsilon1=0
    epsilon2=0
    pb_vectors=[]
    item_k = []
    len_data=0
    N=0                 #用户个数
    F=[]                #频繁项集
    C=[]                #候选项集
    def __init__(self,data,minsup,N,epsilon1,epsilon2,pb_vectors,item_k,len_data,threshold):
        self.data=data
        self.minsup=minsup
        self.N=N
        self.F=[]
        self.C=[]
        self.epsilon1=epsilon1
        self.epsilon2=epsilon2
        self.pb_vectors=pb_vectors
        self.item_k=item_k
        self.len_data=len_data
        self.threshold=threshold
        self.distributioin=[]

    def getFI1(self):
        F=[]
        a=math.exp(self.epsilon1/2)/(1+math.exp(self.epsilon1/2))
        b=1-a
        sum = np.zeros(self.len_data, dtype=np.float64)
        minsup=self.minsup
        for i in range(self.N):
            t=0
            j=0
            mdata=self.data[i]
            mpb_vector=self.pb_vectors[i]
            for k in self.item_k:
                if mpb_vector[j]==0:
                    for index in range(k):
                        #print(t)
                        sum[t]+=mdata[t]
                        t+=1

                elif mpb_vector[j]==1:
                    for index in range(k):
                        if mdata[t]==1:
                            sum[t]+=(1-b)/(a-b)
                        else:
                            sum[t]+=b/(b-a)
                        t+=1
                elif mpb_vector[j]==2:
                    c = math.exp(self.epsilon2) / (k - 1 + math.exp(self.epsilon2))
                    d=(1-c)/(k-1)
                    for index in range(k):
                        if mdata[t]==1:
                            sum[t]+=(1-d)/(c-d)
                        else:
                            sum[t]+=d/(d-c)
                        t+=1
                j+=1
        for i in range(self.len_data):
            if sum[i]>=self.N*self.minsup:
                F.append([int(i/8),int(i%8)])
            self.distributioin.append(sum[i]/self.N)
        return sum,F
    def apriori_gen(self,F,k):
        C=[]
        F_t=[]
        F_m=[]
        a = math.exp(self.epsilon1 / 2) / (1 + math.exp(self.epsilon1 / 2))
        b = 1 - a
        len_data=len(F)
        for i in range(len_data-1):
            for j in range(i+1,len_data):
                if k-2==0:
                    F_m=[]
                    F_m.append(F[i])
                    F_m.append(F[j])
                    C.append(F_m)
                else:
                    if F[i][0:k-2]==F[j][0:k-2]:
                        F_m=[]
                       # F_m.append(F[i][0:k-2])
                        for index in range(k-2):
                            F_m.append(F[i][index])
                        F_m.append(F[i][k-2])
                        F_m.append(F[j][k-2])
                        flag=1
                        F_t=[]
                        for item in F_m:
                            F_t.append(item)
                        for index in range(k-2):
                            del F_t[index]
                            if F_t not in F:
                                flag=0
                                break
                        for index in range(k-1):
                            for index1 in range(index+1,k):
                                if F_m[index][0]==F_m[index1][0]:
                                    flag=0
                                    break
                        if flag==1:
                            C.append(F_m)
        return C
    def apriori_p(self):
        k=1
        F_t=[]
        C_t=[]
        a = math.exp(self.epsilon1 / 2) / (1 + math.exp(self.epsilon1 / 2))
        b = 1 - a
        sum = np.zeros(self.len_data, dtype=np.float64)
        sum,F1=self.getFI1()
        F_t.append(F1)
        while k<self.threshold:
            k=k+1
            C_k=self.apriori_gen(F_t[k-2],k)
            Support=np.zeros(len(C_k), dtype=np.float64)
            for i in range(self.N):
                mdata=self.data[i]
                mpb_vector = self.pb_vectors[i]
                n=0 #表示候选项集的位置
                for itemset in C_k:
                    flag1=1
                    P1 = 1
                    P2 = 1
                    P3 = 1
                    for item in itemset:
                        index=item[0]*8+item[1]
                        P2*=self.distributioin[index]
                        if mpb_vector[item[0]]==0:
                            if mdata[index]==0:
                                flag1=0
                                P1=0
                                break
                        elif mpb_vector[item[0]]==1:
                            if mdata[index]==1:
                                P1*=a
                            else:
                                P1*=b
                        elif mpb_vector[item[0]]==2:
                            mk=self.item_k[item[0]]
                            c = math.exp(self.epsilon2) / (mk - 1 + math.exp(self.epsilon2))
                            d = (1 - c) / (mk - 1)
                            if mdata[index]==1:
                                P1*=c
                            else:
                                P1*=d
                    sum=2**k
                    total_P=0
                    for set in range(sum):
                        Pt1 = 1
                        Pt2 = 1
                        flag2=1
                        j_t=0
                        set=bin(set).replace('0b','')
                        mset=np.zeros(k, dtype=np.int64)
                        for m_i in range(len(set)):
                            mset[k-m_i-1]=set[m_i]
                        for bit_n in range(k):
                            index = itemset[bit_n][0] * 8 + itemset[bit_n][1]
                            if mset[bit_n]==1:
                                Pt2*=self.distributioin[index]
                            else:
                                Pt2*=1-self.distributioin[index]
                        for bit_n in range(k):
                            index=itemset[bit_n][0] * 8 + itemset[bit_n][1]
                            if mpb_vector[itemset[bit_n][0]]==0:
                                if mset[bit_n]==0:
                                    flag2=0
                                    Pt1=0
                                    break
                                else:
                                    Pt1=1
                            elif mpb_vector[itemset[bit_n][0]] == 1:
                                if mset[bit_n] == 1:
                                    Pt1 *= a
                                else:
                                    Pt1 *= b
                            elif mpb_vector[itemset[bit_n][0]] == 2:
                                mk = self.item_k[item[0]]
                                c = math.exp(self.epsilon2) / (mk - 1 + math.exp(self.epsilon2))
                                d = (1 - c) / (mk - 1)
                                if mset[bit_n] == 1:
                                    Pt1 *= c
                                else:
                                    Pt1 *= d
                        if flag2!=0:
                            total_P+=Pt1*Pt2
                    if flag1!=0:
                        Support[n]+=(P1*P2)/total_P
                    n=n+1
            F_k=[]
            for i in range(len(Support)):
                if Support[i]>=self.minsup*self.N:
                    F_k.append(C_k[i])
            F_t.append(F_k)
        return F_t














