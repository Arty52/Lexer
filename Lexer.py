#Art Grichine
#Zeed Jarrah
#ArtGrichine@csu.fullerton.edu
#ZJarrah@csu.fullerton.edu

import sys
import queue
import itertools, collections
from collections import deque
           
#dfs for real, int, ident

# def fsm_int(omega):
#     state = 0                           #starting state
#     table = [[0,0,0,0,0,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1,1,1,1,1]]
#
#     for i in omega:
#         if i.isdigit():
# #            print('i is digit col = int(i): {}'.format(i))
#             col = int(i)
#         else:
#             col = 10
#         state = table[state][col]
# #        print('new state: {}'.format(state))
#
#     if state == 0:
#         return False
#     else:
#         return True

def fsm_int(omega, state):
#    state = 0                           #starting state
    table = [[0,0,0,0,0,0,0,0,0,0,2,1],
             [1,1,1,1,1,1,1,1,1,1,1,1],
             [2,2,2,2,2,2,2,2,2,2,3,3],
             [3,3,3,3,3,3,3,3,3,3,3,3]]
             
    for i in omega:
        if i.isdigit(): 
#            print('i is digit col = int(i): {}'.format(i))
            col = int(i)
        elif i == '.':
            col = 10
        else:
            col = 11
        state = table[state][col]
#        print('new state: {}'.format(state))
    
    return state        

#input: list of elements to process
#output: two lists, tokens and lexemes
def lexer(todo):
    #from p46 of slides
    tokens = []
    lexemes = []
    token = ''
    state = 0               #starting state
    
    while len(todo) > 0:
#    for current in range(len(todo)):
        valid = False
        
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
            
# #        while token.isdigit():
#         while any(char.isdigit for char in token):
#         #check for int
#             token += todo.popleft()             #getchar()
#
#             if fsm_int(token):
#  #               print('fsm_int returns True')
#                 todo.appendleft(token[-1])
#                 token = token[:-1]
#                 tokens.append('integer')
#                 lexemes.append(token)
#                 token = ''
#                 valid = True

#        while token.isdigit():  
        while any(char.isdigit() for char in token):
        #check for int
            print('token: {}'.format(token))
    #        print('todo: {}'.format(todo))
            token += todo.popleft()             #getchar()
            
            if fsm_int(token, state) == 1:
 #               print('fsm_int returns True')
                todo.appendleft(token[-1])
                token = token[:-1]
                tokens.append('integer ')
                lexemes.append(token)
                token = ''
                valid = True
            elif fsm_int(token, state) == 3:
                todo.appendleft(token[-1])
                token = token[:-1]
                tokens.append('real   ')
                lexemes.append(token)
                token = ''
                valid = True
        state = 0   
        
#        print('Token: {}'.format(token))
        #check for keyword
        if check_keyword(token) and valid == False:
           tokens.append('keyword')
           lexemes.append(token)
           token = ''
           valid = True
        
#        print('end: {}'.format(current))
    print('Tokens Remains: {}'.format(token))
    print('Tokens      Lexemes')
    for i in range(len(tokens)):
        print('{}      {}'.format(tokens[i], lexemes[i]))

def check_keyword(token):
   if token == 'int' or token == 'boolean' or token == 'real' or token == 'if' or token == 'else' or token == 'else' or token == 'endif' or token == 'while' or token == 'return' or token == 'read' or token == 'write' or token == 'true' or token == 'false' or token == 'function':
       return True
   else:
       return False
    

def check_operator(c):
    if c == '<' or c == '>' or c == '+' or c == '*' or c == '-' or c == '/' or c == '=':
        return True
    else:
        return False

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