#Art Grichine
#ArtGrichine@csu.fullerton.edu

import sys
import queue
            
#class Cell:
#    def __init__(self, item):
#        self._item = item
        
#    def setMyRow(self, row):
#        self._myrow = row
#    def getMyRow(self):
#        return self._myrow
#    myrow = property(getMyRow, setMyRow)
        
#    def setMyCol(self, col):
#        self._mycol = col
#    def getMyCol(self):
#        return self._mycol
#    mycol = property(getMyCol, setMyCol)
        
#    def setMySubBoard(self, sub):
#        self._mysubboard = sub
#    def getMySubBoard(self):
#        return self.mysubboard
#    mysubboard = property(getMySubBoard, setMySubBoard)
    
#    def __str__(self):
#        return str(self._item)


#class MySubBoard:
 #   def __init__(self, cells):
  #      myCells = set(cells)
   #     for cell in myCells:
    #        cell.mysubboard = self

def identifyType(c):
    type = {'function' : 'keyword',
            'int' : 'keyword',
            'boolean' : 'keyword',
            'real' : 'keyword',
            'if' : 'keyword',
            'else' : 'keyword',
            'endif' : 'keyword',
            'return' : 'keyword',
            'write' : 'keyword',
            'read' : 'keyword',
            'while' : 'keyword',
           }

def main():
    file = []
#    with open(sys.argv[1]) as fh:     #implicitly open and close the file
#    with open(input('Enter file you would like to open: ')) as fh:
    with open('sample.txt') as fh:
        if (fh): 
            print('Open!')
            for i in fh:
                line = i.rstrip()       #strip the EOL
                file.append(line)
                print(line)
        else: 
            print('Not found :-(')
        
        print(file)
#        for i in fh:                   
#            puzzle = i.rstrip()


if __name__ == '__main__':
    main()