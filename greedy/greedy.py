
data=[]
data1 = []
with open('jobs.txt') as f:

    for row in f:
        if len(row.strip().split()) <2 :continue
        weight_  = row.strip().split()[0]
        length_ =  row.strip().split()[1]
        ratio = float(weight_)/float(length_)
        diff_ = int(weight_)-int(length_)
        data.append((diff_,int(weight_),int(length_)))
        data1.append((ratio,int(weight_),int(length_)))

data = sorted(data,key  = lambda x:(x[0],x[1]) ,reverse= True)
data1 = sorted(data1,key = lambda x:x[0],reverse =True) 
sum_ = 0
len_ = 0 
for d,w,l  in data:
    len_ += l 
    sum_ += len_ * w 
        
print(sum_)
len_=0;sum_=0
for r,w,l in data1:
    len_ += l 
    sum_ += len_* w 
print(sum_)
