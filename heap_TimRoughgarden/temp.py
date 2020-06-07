
data = [];median=[]
with open('Median.txt') as f:
    for row in f:
        data.append(int(row.strip().split()[0]))
        data = sorted(data)
          
        median.append( data[int(len(data)/2)-1] if len(data)%2 ==0 else data[int((len(data)+1)/2)-1]  )
       # print(median[-1])

rst = sum(median) % 10000 
print(median)
