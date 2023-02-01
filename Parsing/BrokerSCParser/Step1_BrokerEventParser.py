import re
import glob

path = '/home/javarotti/Repo/Mosquitto/mosquitto-master/**/*.c'
erroFileList = []
noLogFileList = []
logFileList = []

def extractMultipleLine(lines, index):
    result = lines[index].strip()   
    subIndex = index + 1
    while lines[subIndex].strip()[-1] != ';':
        result += lines[subIndex].strip()
        subIndex += 1
    result += lines[subIndex].strip()
    return result

def processFile(fileName):
    try:
        with open(fileName) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
    except Exception as e: 
        print('Error reading file' + fileName + ": " + str(e))
        erroFileList.append(fileName)
        return []

    logList = []
    for index, line in enumerate(lines):
        if (re.search('.*(log).*(print).*', line) != None):
            if (line[-1].strip() == ';'):
                logList.append(line.strip())
            else: 
                logList.append(extractMultipleLine(lines, index))
    
    return logList

fullLogList = []

for file in glob.iglob(path, recursive = True):
    result = processFile(file)
    if(len(result) == 0): 
        noLogFileList.append(file)
        print(file)
    else:
        logFileList.append(file)
        print(file)
    fullLogList += result

file = open("/home/javarotti/Data/ParsedData/SCPartial/step1-sc-event-broker-results.txt", "w+")
for log in fullLogList:
    file.write(log + "\n")
file.close()
