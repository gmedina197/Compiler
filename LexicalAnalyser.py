import re
class LexicalAnalyser:
    #(token, regex)
    #ORDER MATTERS
    RULES = [
        ('MAIN', r'MAIN'),
        ('INT', r'INT'),
        ('FLOAT', r'FLOAT'),
        ('BOOL', r'BOOL'),
        ('IF', r'IF'),
        ('ELSE', r'ELSE'),
        ('WHILE', r'WHILE'),
        ('PRINT', r'PRINT'),
        ('INPUT', r'INPUT'),
        ('LBRACKET', r'\('),
        ('RBRACKET', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('PCOMMA', r';'),
        ('EQ', r'=='),
        ('LE', r'<='),
        ('GE', r'>='),
        ('LT', r'<'),
        ('GT', r'>'),
        ('OR', r'\|\|'),
        ('AND', r'&&'),
        ('NOT', r'!'),
        ('ATTR', r'='),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('MULT', r'\*'),
        ('DIV', r'\/'),
        ('TRUE', r'True'),
        ('FALSE', r'False'),
        ('FLOATN', r'\d(\d)*\.\d(\d)*'),
        ('INTEGER', r'\d(\d)*'),
        ('ID', r'[a-z_A-Z0-9]\w*'),
        ('NEWLINE', r'\n'),
        ('IGNORE', r'[ \t]+'),
        ('MISMATCH', r'.')
    ]

    formatted_rules = "|".join('(?P<%s>%s)' % x for x in RULES)

    line = 1

    def __init__(self):
        #(token, lexeme, row, col)
        self.data = []
    
    def print_tokens(self):
        for token, lexeme, row, col in self.data:
            print(f"Token = {token}, Lexeme = '{lexeme}' Row = {row}, Col = {col}")

    def analyse(self, code):
        line_start = 0 # for col calculation
        for m in re.finditer(self.formatted_rules, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                self.line += 1
                line_start = m.end()
            elif token_type == 'IGNORE':
                continue
            elif token_type == 'MISMATCH':
                raise RuntimeError("{} unexpected on line {}".format(token_lexeme, self.line))
            else:
                col = m.start() - line_start
                data_tuple = (token_type, token_lexeme, self.line, col)
                self.data.append(data_tuple)