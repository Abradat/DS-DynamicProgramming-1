from Grammer import GenerateGrammer
from String import GenerateString

gramAdd = raw_input("Enter the Grammer's address : ")
strAdd = raw_input("Enter the String's address : ")


grammer = GenerateGrammer.Grammer(gramAdd)
strings = GenerateString.String(strAdd)

results = []
for string in strings.strings:
    if(grammer.checkStrToGram(string)):
        results.append(string + ": True")
    else:
        results.append(string + ": False")
print results