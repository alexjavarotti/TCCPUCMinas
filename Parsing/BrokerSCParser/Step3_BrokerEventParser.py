import re

fileName = '/home/javarotti/Data/ParsedData/SCPartial/step2-sc-event-broker-results.txt'

def processFile(fileName):
    try:
        with open(fileName) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines
    except Exception as e: 
        print('Error reading file' + fileName + ": " + str(e))
        return []

result = processFile(fileName)

def extractPattern(inputList, outputList, regExpression, group):
    engine = re.compile(regExpression)
    for item in inputList:
        match = engine.match(item)
        if(match != None):
            outputList.append(match.group(group).strip())

logList = []
extractPattern(result, logList, '"(.*?)"[,.*]*', 1)

file = open("/home/javarotti/Data/ParsedData/SCPartial/step3-sc-event-broker-results.txt", "w+")
for log in logList:
    file.write(str(log) + "\n")
file.close()