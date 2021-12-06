# Smallest Rotation With Highest Score

list1 = [2,3,1,4,0]
scores = []

def new_list_creator(list , k):
    Newlist = []
    difference = []
    current_score = 0    

    while k < len(list):
            Newlist.append(list1[k])
            k +=1

    for i in range(len(list) - len(Newlist)):
        Newlist.append(list[i])

    for i in range(len(Newlist)):
        difference.append(Newlist[i] - i)
    
    for diff in difference:
        if(diff <= 0):
            current_score += 1

    scores.append(current_score)


for i in range(len(list1)):
    new_list_creator(list1 , i)

for score in scores:
    if(score == max(scores)):
        print(scores.index(score))
        break