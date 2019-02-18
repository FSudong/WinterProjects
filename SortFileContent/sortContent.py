
class SortContent:

    fileContent = []
    lineByDict = {}

    def readFile(self, filePath):
        self.fileContent = []
        self.lineByDict = {}
        fp = open(filePath)
        lines = fp.readlines()
        for line in lines:
            line_list = []
            linere = line.replace("\n","")
            if linere:
                self.fileContent.append(linere.split("\t"))
        fp.flush()
        fp.close()
        pass

    def writeFile(self,filePath):
        fp = open(filePath, 'w')
        for item in self.lineByDict.items():
            # lineStr = str(_[1]).replace("[","").replace("]","")
            _ = item[1]
            fp.write(str(_[0])+"\t"+str(_[1])+"\t"+str(_[2]))
            fp.write("\n")
        fp.close()
        pass

    def sortByStudentID(self):
        for line in self.fileContent:
            self.lineByDict[line[0]] = line
        self.lineByDict = dict(sorted(self.lineByDict.items(), key = lambda x:x[0], reverse=False))
        pass

    def sortByName(self):
        for line in self.fileContent:
            self.lineByDict[line[1]] = line
        self.lineByDict = dict(sorted(self.lineByDict.items(), key = lambda x:x[0], reverse=False))
        pass

    def sortByScore(self):
        for line in self.fileContent:
            self.lineByDict[line[2]] = line
        self.lineByDict = dict(sorted(self.lineByDict.items(), key = lambda x:x[0], reverse=False))
        pass


if __name__ == '__main__':
    filePath = "studentInfo.txt"
    sortTool = SortContent()

    # sortTool.sortByName()
    # sortTool.writeFile(filePath)
    while(True):
        print("Now the file content is:")
        sortTool.readFile(filePath)
        print(sortTool.fileContent)
        print("make a choose!!\n1、sort by id\n2、sort by name\n3、sort by score\n4、exit")
        choose = input()
        if choose == "1":
            sortTool.sortByStudentID()
        elif choose == "2":
            sortTool.sortByName()
        elif choose == "3":
            sortTool.sortByScore()
        elif choose == "4":
            break
        sortTool.writeFile(filePath)
    pass