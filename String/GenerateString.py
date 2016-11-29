
class String():

    def __init__(self, stringAddress):
        self.strings = []
        stringFile = open("String/" + stringAddress, 'r')
        for line in stringFile:
            rLine = line.replace('\n', '')
            self.strings.append(rLine)


