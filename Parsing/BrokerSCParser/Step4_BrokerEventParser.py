import re

fileName = '/home/javarotti/Data/ParsedData/SCPartial/step3-sc-event-broker-results.txt'

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

def repladePattern(inputList, outputList):
    for item in inputList:
        common = re.sub("%[cdiefgosuxpn]", "<*>", item)
        outputList.append(common)

logList = []
repladePattern(result, logList)

file = open("/home/javarotti/Data/ParsedData/SCPartial/step4-sc-event-broker-results.txt", "w+")
for log in logList:
    file.write(str(log) + "\n")
file.close()