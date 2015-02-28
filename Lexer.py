#Art Grichine
#Zeed Jarrah
#ArtGrichine@csu.fullerton.edu
#ZJarrah@csu.fullerton.edu

import sys
import queue
import itertools, collections

#Todo: find a way to incriment iterator in for loop

#def consume(iterator, n):
#    collections.deque(itertools.islice(iterator,n))
        
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

def fsm_int(state, omega):
    table = [[2,2,2,2,2,2,2,2,2,2,3],
             [1,1,1,1,1,1,1,1,1,1,3],
             [1,1,1,1,1,1,1,1,1,1,1]]
#    state = 1       #starting state
    for i in omega:
        if i.isdigit: 
            col = int(i)
        else:
            col = 10
        state = table[state][col]
        print('new state: {}'.format(state))
    if state == 1:  
        return True
    else:
        return False
    
    

#input: list of elements to process
#output: two lists, tokens and lexemes
def lexer(todo):
    #from p46 of slides
    tokens = []
    lexemes = []
    token = ''
    state = 1
    
    while len(todo) > 0:
#    for current in range(len(todo)):
        valid = False
        
        #if the top of the stack contains a space, pop it off
        while todo[0].isspace():
            todo.pop(0)
        
        token += todo.pop(0)
        
#        print('beginning: {}'.format(current))
        #handle two character operators
        if todo:                                    #if todo not empty
            if token == ':' and todo[0] == '=':
                tokens.append('operator')
                lexemes.append(':=')
                todo.pop(0)
                token = ''
                valid = True

            if token == '=' and todo[0] == '>':
                tokens.append('operator')
                lexemes.append('=>')
                todo.pop(0)
                token = ''
                valid = True

            if token == '<' and todo[0] == '=':
                tokens.append('operator')
                lexemes.append('<=')
                todo.pop(0)
                token = ''
                valid = True

            if token == '!' and todo[0] == '=':
                tokens.append('operator')
                lexemes.append('!=')
                todo.pop(0)
                token = ''
                valid = True
        
        #handle two character separators
            if token == '@' and todo[0] == '@':
                tokens.append('operator')
                lexemes.append('@@')
                todo.pop(0)
                token = ''
                valid = True

            if token == '/' and todo[0] == '*':
                tokens.append('operator')
                lexemes.append('/*')
                todo.pop(0)
                token = ''
                valid = True

            if token == '*' and todo[0] == '/':
                tokens.append('operator')
                lexemes.append('*/')
                todo.pop(0)
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
            
            # if fsm_int(state,token):
 #                print(state)
 #            else:
 #                print('not int')
                    
        if fsm_int(state, token) and valid == False:
            print('fsm_TRUE, valid_False!')
            tokens.append('integer')
            lexemes.append(token)
            token = ''
            valid = True
        
        # if valid == False:
        #     token += todo[current]
        
#        if token.isdigit:         
        
        print('Token: {}'.format(token))
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