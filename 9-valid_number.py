import re

s = "53.5e93"
decimal1_minus = r"-?\d+\.\d{0,}"
decimal2_minus = r"-?\.\d+"
decimal1_with_e_minus = r"-?\d+\.\d{1,}e\W{0,1}\d{1,}"
decimal2_with_e_minus = r"-?\.\d+e\W{0,1}\d{1,}"
decimal1_plus = r"\+?\d+\.\d{0,}"
decimal2_plus = r"\+?\.\d+"
decimal1_with_e_plus = r"\+?\d+\.\d{1,}e\W{0,1}\d{1,}"
decimal2_with_e_plus = r"\+?\.\d+e\W{0,1}\d{1,}"

integer_plus = r"\+?\d+"
integer_minus = r"-?\d+"
integer_with_e_plus = r"\+?\d+e\W{0,1}\d{1,}"
integer_with_e_minus = r"-?\d+e\W{0,1}\d{1,}"

if (re.fullmatch(decimal1_plus , s) != None):
    print(True)
elif ((re.fullmatch(decimal2_plus , s)) != None):
    print(True)
elif (re.fullmatch(decimal1_with_e_plus, s) != None):
    print(True)
elif (re.fullmatch(decimal2_with_e_plus , s) != None):
    print(True)
elif (re.fullmatch(decimal1_minus , s) != None):
    print(True)
elif (re.fullmatch(decimal2_minus , s) != None):
    print(True)
elif (re.fullmatch(decimal1_with_e_minus , s) != None):
    print(True)
elif (re.fullmatch(decimal2_with_e_minus , s) != None):
    print(True)
elif (re.fullmatch(integer_plus , s) != None):
    print(True)
elif (re.fullmatch(integer_minus , s) != None):
    print(True)
elif (re.fullmatch(integer_with_e_plus , s) != None):
    print(True)
elif (re.fullmatch(integer_with_e_minus , s) != None):
    print(True)
else:
    print(False)