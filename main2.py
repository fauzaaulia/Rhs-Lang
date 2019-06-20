import rhs_lexer
import rhs_parser
import rhs_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = rhs_lexer.BasicLexer()
    parser = rhs_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('RHS > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            rhs_interpreter.BasicExecute(tree, env)
