class SemanticException(Exception):
    def __init__(self, message, token):
        row = token[2]
        col = token[3]

        self.message = message + f' at line {row} column {col}'
        
    def __str__(self):
        return self.message