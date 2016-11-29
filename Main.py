from Grammer import GenerateGrammer
from String import GenerateString

gramAdd = raw_input("Enter the Grammer's address : ")
strAdd = raw_input("Enter the String's address : ")
outAdd = raw_input("Enter the output's file address : ")

grammer = GenerateGrammer.Grammer(gramAdd)
strings = GenerateString.String(strAdd)

results = []
for string in strings.strings:
    if(grammer.checkStrToGram(string)):
        results.append(string + ": True")
    else:
        results.append(string + ": False")

outFile = open("Output/" + outAdd, 'w')
for result in results:
    outFile.write(result + "\n")
outFile.close()