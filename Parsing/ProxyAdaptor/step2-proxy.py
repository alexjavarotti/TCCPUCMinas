# ABB.Ability.IoTEdge.EdgeAgent.Services.CommonDiagnosticCheckService[0]
# [2022-10-21T13:23:16.4215035Z]
# : Diagnostic Check is pass. {"ENABLE_ ...

import re

input_dir = '/home/javarotti/Data/ParsedData/ProxyPartial/' # The input directory of log file
output_dir = '/home/javarotti/Data/ParsedData/ProxyPartial/' # The output directory of parsing results
log_file = 'abb-edge-19-proxy-5.log' # The input log file name
step1tag = 'step1-'
step2tag = 'step2-'

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
        match = engine.match(item)#.replace(' ',''))
        if(match != None):
            trash = match.group(1)
            component = match.group(2).strip()
            timestamp = match.group(3).replace('[','').replace(']','').strip()
            content = removeMultiSpace(match.group(4).removeprefix(': '))
           
            outputList.append(timestamp + ';' + component + ':' + content)

def removeMultiSpace(input):
    return re.sub(' +', ' ', input)

def extractTimeStamp(input):
    return input.replace('[','').replace(']','').strip()

result = processFile(input_dir + step1tag + log_file)
logList = []
extractPattern(result, logList, '(.*?:)(.*\[[0-9]\])(\s*\[.*T.*Z\])(.*)')

file = open(output_dir + step2tag + log_file, "w+")
for log in logList:
    file.write(str(log) + '\n')
file.close()
