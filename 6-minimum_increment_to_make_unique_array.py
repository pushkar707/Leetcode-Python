numbers = [5,4,3,2,2,2,2,2,2,2,2,2]
moves  = 0
new_nums = []
new_nums.append(numbers[0])

for num in numbers[1:]:    
    for i in range(len(numbers)):
        for new_num in new_nums:
            if num == new_num:
                moves += 1
                num += 1
    new_nums.append(num)

print(moves)
print(new_nums)