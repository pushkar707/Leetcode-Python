head = [1,2,3,4,5]
k = 6
newhead = []


index = 0

for i in range(k):
    newhead.insert(0,head[len(head)+index-1])
    index -= 1

for num in head[:len(head)-k]:
    newhead.append(num)

print(newhead[:len(head)])