import re
logs = ["d1/","d2/","./","d3/","../","d31/"]
folder_level = 0

def log_checker(log):    
    global folder_level

    # New Folder
    pattern = r"\w+/"
    if len(re.findall(pattern , log)) == 1:
        folder_level += 1
    elif log == '../':
        folder_level -= 1
    elif log == './':
        pass

    if folder_level < 0:
        folder_level = 0

for log in logs:
    log_checker(log)

print(folder_level) 