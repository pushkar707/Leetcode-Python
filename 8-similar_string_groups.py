strs = ["omv","ovm"]
groups = []
answer = 0

# First Read Below Comment
def compare_groups(grp):
    global answer

    word1 = grp[0]
    word2 = grp[1]

    unequal_letter1 = set()
    unequal_letter2 = set()
    unequal_letters = 0

    for index1 , letter1 in enumerate(word1):
        for index2 ,  letter2 in enumerate(word2):
            if index1 == index2:
                if(letter1 == letter2):
                    pass
                else:
                    unequal_letter1.add(letter1)
                    unequal_letter2.add(letter1)
                    unequal_letters += 1

    for i , letter in enumerate(unequal_letter1):
        if i == 0:
            letter_1 = letter
        elif i == 1:
            letter_2 = letter
        else:
            pass
    if unequal_letters == 2 and unequal_letter1 == unequal_letter2:
        word1 = word1.replace(letter_1 , letter_2)
        word2 = word2.replace(letter_1 , letter_2)

    if word1 == word2:
        answer += 1

# Start Here
# This is done to divide strs in groups of two words so that letter of those words could be compared.
for word in strs:
    if len(groups) < 2:
        groups.append(word)
        if len(groups) == 2:
            compare_groups(groups)
    else:
        groups.pop(0)
        groups.append(word)
        compare_groups(groups)

print(answer)