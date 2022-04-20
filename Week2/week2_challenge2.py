data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251", "조회수: 13,432", "조회수: 998"]
sum = 0

#1
for i in range(len(data)):
    print(data[i])

#2
for k in data:
    k = k[5:]
    k = k.replace(",", "")
    print(k)

#3
for j in data:
    j=j[5:]
    j = j.replace(",", "")
    sum+=int(j)

print("총합 : ", sum)