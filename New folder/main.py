import rhs_lexer
import rhs_parser
import rhs_interpreter

lexer = rhs_lexer.BasicLexer()
parser = rhs_parser.BasicParser()
env = {}

text = ""
with open('bahasaku.rhs', 'r') as file:
    text = file.read()
#text = input('basic > ')

tree = parser.parse(lexer.tokenize(text))
rhs_interpreter.BasicExecute(tree, env)