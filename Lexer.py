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
           
#dfs for real, int, ident
#def fsm_operator():
#    state_table = []
    

#input: list of elements to process
#output: two lists, tokens and lexemes
def lexer(todo):
    #from p46 of slides
    tokens = []
    lexemes = []
    
    for current in range(len(todo)):
        token = todo[current]
        if check_seperator(token):
            tokens.append(token)
    print(tokens)
    
    #begin
    #   repeat
    #       getchar()
    #       if input char terminates a token AND it is an accepting state then
    #           isolate the token/lexeme
    #           decrement the CP if necessary
    #       else lookup FSM (current state, input char)
    #   until (token found) or (no more input)
    
    #   if token found then 
    #       return token
    #end

#input: character from todo
#output:
def check_seperator(c):
    if c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']' or c == ':' or c == ';' or c == ',':
        return True
    else:
        return False

#def check_operator():

#def check_keywork():


#process file and prepare list of characters to process
#input: none
#output: List of characters that are in text file          
def process_file():
    file = []
    todo = []
    
    #open file
#    with open(sys.argv[1]) as fh:     #implicitly open and close the file from commandline
#    with open(input('Enter file you would like to open: ')) as fh:
    with open('sample.txt') as fh:          #implicitly open and close the file
        if (fh): 
            print('Open!')
            for i in fh:
                line = i.strip()       #strip the 
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
    todo = []             #list of characters left to process
    todo = process_file()
    print(todo)
    lexer(todo)

if __name__ == '__main__':
    main()