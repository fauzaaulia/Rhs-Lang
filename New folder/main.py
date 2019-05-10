import rhs_lexer
import rhs_parser
import rhs_interpreter

from sys import *

#DENGAN MASUKAN BAHASAKU.RHS
lexer = rhs_lexer.BasicLexer()
parser = rhs_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    rhs_interpreter.BasicExecute(tree, env)

#MASUKAN LANGSUNG
# if __name__ == '__main__':
#     lexer = rhs_lexer.BasicLexer()
#     parser = rhs_parser.BasicParser()
#     env = {}
#     while True:
#         try:
#             text = input('RHS > ')
#         except EOFError:
#             break
#         if text:
#             tree = parser.parse(lexer.tokenize(text))
#             rhs_interpreter.BasicExecute(tree, env)
