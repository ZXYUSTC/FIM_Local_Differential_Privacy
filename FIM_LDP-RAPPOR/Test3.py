fo=open('data-raw.txt','r+')
test = fo.readline()
first = test.split()
print(first)
F_score=[]

fo1=open('data1.txt')
test=fo1.readline()
while test:
    second=test.split()
    sum=0.0
    for item in second:
        if item in first:
            sum+=1.0
    precision=sum/len(second)
    recall=sum/len(first)
    F_score.append(2*(precision*recall)/(precision+recall))
    test=fo1.readline()
'''
tmp=test.split()
i=0
mdata=[]
print(tmp)
for data in tmp:
    i=i+1
    mdata.append(data)
    if i%2==0:
        second.append(mdata)
        mdata=[]
print(second)
'''
print(F_score)
fo.close()
fo1.close()
