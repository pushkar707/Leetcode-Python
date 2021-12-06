import math

s = "abcdef"
k = 4
new_string = ''
sub_strings = []
moves = 0

for index , letter in enumerate(s):
    new_string += letter
    if((index+1)%k == 0):
        sub_strings.append(new_string)
        new_string = ''

if len(s)%k != 0:
    sub_strings.append(s[-(len(s)%k):])

for str in sub_strings:
    for i in range(math.floor(len(str)/2)):
        if str[i] != str[-i-1]:
            print(str.replace(str[-i-1] , str[i]))
            # print(str)
            moves += 1
    # print(str)

print(sub_strings)
print(moves)