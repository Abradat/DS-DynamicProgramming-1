class Grammer():

    def __init__(self, grammerAddress):
        self.gramDict= {}
        gramFile = open("Grammer/" + grammerAddress, 'r')
        for line in gramFile:
            rLine = line.replace(' ', '').replace('\n', '').split('->')
            self.gramDict[rLine[0]] = rLine[1].split('|')
            #print self.gramDict

    def checkStrToGram(self, string):
        self.matris = []
        strLen = len(string)
        for cnt in range(strLen):
            self.matris.append([])
        #self.printMatris()

        for cnt2 in range(strLen):
            for cnt3 in range(cnt2):
                self.matris[cnt2].append(['-'])
            self.matris[cnt2].append(self.checkGram(string[cnt2]))
        #self.printMatris()

        div = 1
        for rowCnt in range(1, strLen):
            for inRowCnt in range(strLen - rowCnt):
                fRes = []
                res = []
                for k in range(inRowCnt, inRowCnt + div):
                    merged = self.mergeString(self.matris[inRowCnt][k], self.matris[k + 1][inRowCnt + div])
                    #print merged
                    for mergedCnt in merged:
                        fRes.append(mergedCnt)
                        #print fRes
                for fResCnt in fRes:
                    aux = self.checkGram(fResCnt)
                    for auxCnt in aux:
                        #print auxCnt
                        res.append(auxCnt)
                res = set(res)
                res = list(res)

                if(len(res) != 1 ):
                    while('0' in res):
                        res.remove('0')
                self.matris[inRowCnt].append(res)
            div += 1

        #self.printMatris()
        if('S' in self.matris[0][strLen - 1]):
            return True
        else:
            return False

    def mergeString(self, C1, C2):
        res = []
        for c1 in C1:
            for c2 in C2:
                res.append(c1 + c2)
        return res

    def checkGram(self, sample):
        filler = []
        for dic in self.gramDict:
            if(sample in self.gramDict[dic]):
                filler.append(dic)
        if(len(filler) != 0):
            return filler
        else:
            return ["0"]

    def printMatris(self):
        for mat in self.matris:
            print mat

x = Grammer("test.txt")
#x.checkStrToGram("baaba")
#print(x.checkGram("BC"))
#x.mergeString(['A', 'C'], ['B', 'C', 'A'])
