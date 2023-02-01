
import re

input_dir = '/home/javarotti/Data/RawData/' # The input directory of log file
output_dir = '/home/javarotti/Data/ParsedData/CSConnectPartial/' # The output directory of parsing results
log_file = 'abb-edge-19-csconnect-1-copy.log' # The input log file name
step1tag = 'step1-'

def processFile(fileName):
    try:
        with open(fileName) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines
    except Exception as e: 
        print('Error reading file' + fileName + ": " + str(e))
        return []

def extractPattern(inputList, outputList, regExpression):
    engine = re.compile(regExpression)
    for item in inputList:
        match = engine.match(item)
        if(match != None):
            timestamp = match.group(1)
            event = match.group(2).strip()
            process = match.group(3)
            outputList.append(timestamp + ';' + event + ";" + process)

result = processFile(input_dir + log_file)
logList = []
pattern1 = '.*([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\.[0-9]{3}.*[A-Z]{3}\](.*)(\[.*\])'

extractPattern(result, logList, pattern1)

file = open(output_dir + step1tag + log_file, "w+")
for log in logList:
    file.write(str(log) + '\n')
file.close()
