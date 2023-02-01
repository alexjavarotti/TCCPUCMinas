import re
import secrets

fileName = '/home/javarotti/Data/ParsedData/SCPartial/step4-sc-event-broker-results.txt'

def processFile(fileName):
    try:
        with open(fileName) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines
    except Exception as e: 
        print('Error reading file' + fileName + ": " + str(e))
        return []

logList = []

result = processFile(fileName)
unique = list(set(result))

for item in unique:
    uuid = secrets.token_hex(8)
    logList.append(uuid + ";" + item)

file = open("//home/javarotti/Data/ParsedData/SCPartial/step5-sc-event-broker-results.txt", "w+")
for log in logList:
    file.write(str(log) + "\n")
file.close()