


# def analyze_code(input_line): 

#    i = 0

#    while i < len(input_line):

#        ch = input_line[i]

#        if ch.isspace():

#            i += 1

#            continue

#        if ch.isalpha() or ch == '_':

#            lexeme = ch

#            i += 1

#            while i < len(input_line) and (input_line[i].isalnum() or input_line[i] == '_'):

#                lexeme += input_line[i]

#                i += 1

#            print("IDENTIFIER:", lexeme)

#            continue

#        elif ch.isdigit():

#            lexeme = ch

#            i += 1

#            while i < len(input_line) and input_line[i].isdigit():

#                lexeme += input_line[i]

#                i += 1

#            print("NUMBER:", lexeme)

#            continue

#        elif ch in "+-*/=()":

#            print("OPERATOR or SYMBOL:", ch)

#            i += 1

#        else:

#            print("UNKNOWN:", ch)

#            i += 1


def analyze_code(input_line): 
    i = 0
    while i < len(input_line):
        ch = input_line[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isalpha() or ch == '_':
            lexeme = ch
            i += 1
            while i < len(input_line) and (input_line[i].isalnum() or input_line[i] == '_'):
                lexeme += input_line[i]
                i += 1
            print("IDENTIFIER:", lexeme)
            continue

        elif ch.isdigit():
            lexeme = ch
            i += 1
            while i < len(input_line) and input_line[i].isdigit():
                lexeme += input_line[i]
                i += 1
            print("NUMBER:", lexeme)
            continue

        elif ch in "+-*/=()":
            print("OPERATOR or SYMBOL:", ch)
            i += 1

        else:
            print("UNKNOWN:", ch)
            i += 1


# Read from 'file.in'
try:
    with open("file.in", "r") as f:
        for line in f:
            analyze_code(line)
except FileNotFoundError:
    print("Error: file.in not found.")
