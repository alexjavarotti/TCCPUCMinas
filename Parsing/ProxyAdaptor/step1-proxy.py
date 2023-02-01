import re

input_dir = '/home/javarotti/Data/RawData/' # The input directory of log file
output_dir = '/home/javarotti/Data/ParsedData/ProxyPartial/' # The output directory of parsing results
log_file = 'abb-edge-19-proxy-5.log' # The input log file name
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
            noBreakLine = item.strip()
            outputList.append('\n' + noBreakLine)
        else:
            outputList.append(item)

result = processFile(input_dir + log_file)
logList = []
extractPattern(result, logList, '.*\\[[0-9]+m.*\\[[0-9]+[a-z]+.*\\[[0-9]+m.*\\[[0-9]+m.*\\[[0-9]+m:.*')

file = open(output_dir + step1tag + log_file, "w+")
for log in logList:
    file.write(str(log))
file.close()
