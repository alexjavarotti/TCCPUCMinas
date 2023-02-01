import re

input_dir       = '/home/javarotti/Data/RawData/' # The input directory of log file
output_dir      = '/home/javarotti/Data/ParsedData/SCPartial/' # The output directory of parsing results
log_file        = 'abb-edge-19-broker-5.log' # The input log file name

def processFile(fileName):
    try:
        with open(fileName) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines
    except Exception as e: 
        print('Error reading file' + fileName + ": " + str(e))
        return []

result = processFile(input_dir + log_file)

def extractPattern(inputList, outputList, regExpression):
    engine = re.compile(regExpression)
    for item in inputList:
        match = engine.match(item)
        if(match != None):
            outputList.append(match.group(1).strip() + ";" + match.group(2).strip())

logList = []

# The first group repesents the time stamp and the second the log message
extractPattern(result, logList, '([0-9]+):(.*)')

file = open(output_dir + log_file, "w+")
for log in logList:
    file.write(str(log) + "\n")
file.close()