""" This is meant to demonstrate how easy it is to throw the functions from phist into a framework """

from sys import argv
from phist import *


class phistAction:
    def __init__(self, *args):
        self.hashDirectory = 0
        self.hashFile = 0
        self.directoryCheck = 0
        self.fileCheck = 0
        self.delete = 0
        
        # Should be using argParse but I did it in 5 minutes.
        
        
        if argv[1] == "-dh":
            self.hashDirectory = 1
            self.dirToHash = argv[2]
            self.flatDbName = argv[3]
        elif argv[1] == "-fh":
            self.hashFile = 1
            self.fileToHash = argv[2]
            self.flatDbName = argv[3]
        elif argv[1] == "-dc":
            self.directoryCheck = 1
            self.queryDirectory = argv[2]
            self.flatDbName = argv[3]
        elif argv[1] == "-fc":
            self.fileCheck = 1
            self.fileName = argv[2]
            self.flatDbName = argv[3]
        elif argv[1] == "-delete":
            self.delete = 1
            self.flatDbName = argv[2]

        if self.hashDirectory == 1:
            self.hDirectory()
        elif self.hashFile == 1:
            self.hFile()
        elif self.directoryCheck == 1:
            self.cDirectory()
        elif self.fileCheck == 1:
            self.cFile()
        elif self.delete == 1:
            delete(self.flatDbName)
        else:
            print("Command line options are:\n\t <-dh(hash directory), -ih(hash file), -dc(check directory), -ic(check file)> queriedPath flatFile\nOr to delete:\n\t -delete flatFile")


    def hDirectory(self):
        hashDirectory(self.dirToHash, self.flatDbName)
        
    def hFile(self):
        hashFile(self.fileToHash, self.flatDbName)

    def cFile(self):
        returned = fileChecker(self.fileName)
        print(returned)

    def cDirectory(self):
        returned = directoryChecker(self.queryDirectory)
        
        print("\n\tFile Queried:\t\tFile Matched:\t\tDate Entered:\n")
        for i in returned:
           
            s = "\t" + str(i[0].split("/")[-1]) + ":"
            
          
            while len(s) < 20:
                s += " "
                
            s += "\t"  + i[1][2][0][0] + "\t""\t" + i[1][2][0][1] 
            print(s)      
        print("\n") 
    


a = phistAction()
