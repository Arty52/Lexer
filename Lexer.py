#Art Grichine
#ArtGrichine@csu.fullerton.edu

import sys
import queue

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
          
#process file and prepare list of characters to process
#input: none
#output: List of characters that are in text file          
def process_file():
    file = []
    todo = []
    
    #open file
    #    with open(sys.argv[1]) as fh:     #implicitly open and close the file
    with open(input('Enter file you would like to open: ')) as fh:
#    with open('sample.txt') as fh:          #implicitly open and close the file
        if (fh): 
            print('Open!')
            for i in fh:
                line = i.rstrip()       #strip the EOL
                file.append(line)
#                print(line)            #DEBUG
        else: 
            print('Not found :-(')
    
    #for each element 
    for i in file:
 #       print('for i in file = {}'.format(i))      #DEBUG
        for j in i:
            todo.append(j)
    
    return todo

def main():
    todo = []   #list of characters left to process
    todo = process_file()
    print(todo)


if __name__ == '__main__':
    main()