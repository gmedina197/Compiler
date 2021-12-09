class LexicalAnalyser:
    #(token, regex)
    RULES = [
        ('MAIN', r'MAIN'),
        ('INT', r'INT'),
        ('FLOAT', r'FLOAT'),
        ('BOOL', r'BOOL'),
        ('IF', r'IF'),
        ('ELSE', r'ELSE'),
        ('PRINT', r'PRINT'),
        ('INPUT', r'INPUT'),
        ('WHILE', r'WHILE'),
        ('LBRACKET', r'\('),
        ('RBRACKET', r'\)'),
        ('PCOMMA', r';'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
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
        ('ID', r'[a-z_A-Z0-9]\w*'),
        ('FLOAT', r'\d(\d)*\.\d(\d)*'),
        ('INTEGER', r'\d(\d)*'),
        ('NEWLINE', r'\n'),
        ('TAB', r'[ \t]+'),
        ('MISMATCH', r'.')
    ]

    formatted_rules = "|".join(["(?P<{}>{})".format(name, regex) for name, regex in RULES])

    def __init__(self):
        #(token, lexeme, row, col)
        self.data = []
    
    def analyse(self, code):
        print(self.formatted_rules)