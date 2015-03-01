#Art Grichine
#Zeed Jarrah
#ArtGrichine@csu.fullerton.edu
#ZJarrah@csu.fullerton.edu

import sys
import queue
import itertools, collections
from collections import deque
           
#dfs for real, int, ident

#input: list of elements to process and current machine state
#output: machine state value
def fsm_digits(omega, state):
    table = [[0,0,0,0,0,0,0,0,0,0,2,1],
             [1,1,1,1,1,1,1,1,1,1,1,1],
             [2,2,2,2,2,2,2,2,2,2,3,3],
             [3,3,3,3,3,3,3,3,3,3,3,3]]
             
    for i in omega:
        if i.isdigit(): 
            col = int(i)
        elif i == '.':
            col = 10
        else:
            col = 11
        state = table[state][col]
    
    return state        

#input: list of elements to process and current machine state
#output: machine state value
def fsm_identifier(omega, state):
    table = [[1,0,0,3],
             [1,2,2,3],
             [1,2,2,4],
             [3,3,3,3],
             [4,4,4,4]]
             
    for i in omega:
        if i.isalpha():
            col = 0
        elif i.isdigit():
            col = 1
        elif i == '_':
            col = 2
        else:
            col = 3
        state = table[state][col]
    
    return state     
    
#input: list of elements to process and current machine state
#output: two lists, tokens and lexemes
def lexer(todo):
    #from p46 of slides
    tokens = []
    lexemes = []
    token = ''
    
    while len(todo) > 0:
#    for current in range(len(todo)):
        valid = False
        state = 0               #starting state
        
        #if the top of the stack contains a space, pop it off
        while todo[0].isspace():
            todo.popleft()
        
        token += todo.popleft()
        
#        print('beginning: {}'.format(current))
        #handle two character operators
        if todo:                                    #if todo not empty
            if token == ':' and todo[0] == '=':
                tokens.append('operator')
                lexemes.append(':=')
                todo.popleft()
                token = ''
                valid = True

            if token == '=' and todo[0] == '>':
                tokens.append('operator')
                lexemes.append('=>')
                todo.popleft()
                token = ''
                valid = True

            if token == '<' and todo[0] == '=':
                tokens.append('operator')
                lexemes.append('<=')
                todo.popleft()
                token = ''
                valid = True

            if token == '!' and todo[0] == '=':
                tokens.append('operator')
                lexemes.append('!=')
                todo.popleft()
                token = ''
                valid = True
        
        #handle two character separators
            if token == '@' and todo[0] == '@':
                tokens.append('operator')
                lexemes.append('@@')
                todo.popleft()
                token = ''
                valid = True

            if token == '/' and todo[0] == '*':
                tokens.append('operator')
                lexemes.append('/*')
                todo.popleft()
                token = ''
                valid = True

            if token == '*' and todo[0] == '/':
                tokens.append('operator')
                lexemes.append('*/')
                todo.popleft()
                token = ''
                valid = True
        
            #check for separator           
    #        if check_seperator(todo[current]) and valid == False:
        if check_seperator(token) and valid == False:
            tokens.append('separator')
            lexemes.append(token)
            token = ''
            valid = True
            
        #check for operator
        if check_operator(token) and valid == False:
            tokens.append('operator')
            lexemes.append(token)
            token = ''
            valid = True

        #check for int and real
        while token and token[0].isdigit():
#        while any(char.isdigit() for char in token):
            if todo:
                token += todo.popleft()                      #getchar()
            elif any(char == '.' for char in token):
                tokens.append('real   ')
                lexemes.append(token)
                token = ''
                break
            else:
                tokens.append('integer ')
                lexemes.append(token)
                token = ''
                break
            
            if fsm_digits(token, state) == 1:
                todo.appendleft(token[-1])
                token = token[:-1]
                tokens.append('integer ')
                lexemes.append(token)
                token = ''

            elif fsm_digits(token, state) == 3:
                todo.appendleft(token[-1])
                token = token[:-1]
                tokens.append('real   ')
                lexemes.append(token)
                token = ''

            continue            #return to the top of the loop
        
        #check for identifier
        while token and token[0].isalpha():
            if todo:
                token += todo.popleft()
            else:
                break
        
            if fsm_identifier(token, state) == 3:
                todo.appendleft(token[-1])
                token = token[:-1]
                tokens.append('identifier')
                lexemes.append(token)
                token = ''

            #check for keyword
            if check_keyword(token) and valid == False:
               tokens.append('keyword')
               lexemes.append(token)
               token = ''

        
#        print('end: {}'.format(current))
    print('Tokens Remains: {}'.format(token))
    print('{0:14}{1:8}'.format('Tokens', 'Lexemes'))
    for i in range(len(tokens)):
        print('{0:14}{1:8}'.format(tokens[i], lexemes[i]))

def check_keyword(token):
   if token == 'int' or token == 'boolean' or token == 'real' or token == 'if' or token == 'else' or token == 'else' or token == 'endif' or token == 'while' or token == 'return' or token == 'read' or token == 'write' or token == 'true' or token == 'false' or token == 'function':
       return True
   else:
       return False
    
#input: token
#output: true if single character separator, otherwise return false
def check_operator(c):
    if c == '<' or c == '>' or c == '+' or c == '*' or c == '-' or c == '/' or c == '=':
        return True
    else:
        return False

#input: token
#output: true if single character separator, otherwise return false
def check_seperator(c):
    if c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']' or c == ':' or c == ';' or c == ',':
        return True
    else:
        return False


#process file and prepare list of characters to process
#input: none
#output: List of characters that are in text file          
def process_file():
    file = []
    todo = deque()    
    #open file
#    with open(sys.argv[1]) as fh:     #implicitly open and close the file from commandline
#    with open(input('Enter file you would like to open: ')) as fh:
    with open('sample3.txt') as fh:          #implicitly open and close the file
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
        print(i)      #DEBUG
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