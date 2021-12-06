words = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]

output = []
valid_words = 0
letters_in_puzzle = 0

for puzzle in puzzles:
    for word in words:
        for letter in word:            
            if letter == puzzle[0]:
                for letter in word:
                    if letter in puzzle:
                        letters_in_puzzle += 1          
                break
               
        if letters_in_puzzle == len(word):
            valid_words += 1
            letters_in_puzzle = 0
        else:
            letters_in_puzzle = 0
            
    output.append(valid_words)
    valid_words = 0

print(output)