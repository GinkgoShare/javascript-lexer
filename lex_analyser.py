import ply.lex as lex

def test_lexer(lexer,input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result
  
tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

def t_delcomment(token):
    r'/\*[^\*/]*\*/'
    pass

def t_eolcomment(token):
    r'//[^\n]*'
    pass

def t_ANDAND(token):
    r'&&'
    token.type = 'ANDAND'
    return token

def t_COMMA(token):
    r','
    token.type = 'COMMA'
    return token

def t_DIVIDE(token):
    r'/'
    token.type = 'DIVIDE'
    return token

def t_ELSE(token):
    r'else'
    token.type = 'ELSE'
    return token

def t_EQUALEQUAL(token):
    r'=='
    token.type = 'EQUALEQUAL'
    return token

def t_EQUAL(token):
    r'='
    token.type = 'EQUAL'
    return token

def t_FALSE(token):
    r'false'
    token.type = 'FALSE'
    return token

def t_FUNCTION(token):
    r'function'
    token.type = 'FUNCTION'
    return token

def t_GE(token):
    r'>='
    token.type = 'GE'
    return token

def t_GT(token):
    r'>'
    token.type = 'GT'
    return token

def t_IF(token):
    r'if'
    token.type = 'IF'
    return token

def t_LBRACE(token):
    r'{'
    token.type = 'LBRACE'
    return token

def t_LE(token):
    r'<='
    token.type = 'LE'
    return token

def t_LPAREN(token):
    r'\('
    token.type = 'LPAREN'
    return token

def t_LT(token):
    r'<'
    token.type = 'LT'
    return token

def t_MINUS(token):
    r'-'
    token.type = 'MINUS'
    return token

def t_NOT(token):
    r'!'
    token.type = 'NOT'
    return token

def t_OROR(token):
    r'\|\|'
    token.type = 'OROR'
    return token

def t_PLUS(token):
    r'\+'
    token.type = 'PLUS'
    return token

def t_RBRACE(token):
    r'}'
    token.type = 'RBRACE'
    return token

def t_RETURN(token):
    r'return'
    token.type = 'RETURN'
    return token

def t_RPAREN(token):
    r'\)'
    token.type = 'RPAREN'
    return token

def t_SEMICOLON(token):
    r';'
    token.type = 'SEMICOLON'
    return token

def t_TIMES(token):
    r'\*'
    token.type = 'TIMES'
    return token

def t_TRUE(token):
    r'true'
    token.type = 'TRUE'
    return token

def t_VAR(token):
    r'var'
    token.type = 'VAR'
    return token

def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]+)?'
    token.value = float(token.value)
    token.type = 'NUMBER'
    return token

def t_STRING(token):
    r'\"(?:[^\\]|[\\"])*\"'
    token.value = token.value[1:-1]
    token.type = 'STRING'
    return token

def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    token.type = 'IDENTIFIER'
    return token

t_ignore = ' \t\v\r' # whitespace 

def t_newline(token):
        r'\n'
        token.lexer.lineno += 1

def t_error(token):
        print ("JavaScript Lexer: Illegal character " + token.value[0])
        token.lexer.skip(1)

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own. 

lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print (test_lexer(input1) == output1)

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print (test_lexer(input2) == output2)