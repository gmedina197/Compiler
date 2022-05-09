TERMINALS = [
    "main",
    "if",
    "else",
    "+",
    "-",
    "*",
    "/",
    "while",
    "input",
    "print",
    ";",
    "=",
    "int",
    "float",
    "bool",
    "}",
    "{",
    "(",
    ")",
    "True",
    "False",
    "==",
    ">=",
    "<=",
    ">",
    "<",
    "and",
    "or",
    "!"
]

NON_TERMINALS = [
    "S'",
    "PROGRAM",
    "CMD",
    "EXPR",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "DECL",
    "IF",
    "ELSE",
    "ATTR",
    "EXPR_AR",
    "AUX_AR",
    "AUX_AR_F",
    "WHILE",
    "INPUT",
    "PRINT",
    "SEMICOLON",
    "VAR",
    "SET",
    "TIPO",
    "RBRACE",
    "LBRACE",
    "LPAR",
    "RPAR",
    "INTEGER",
    "FLOAT_N",
    "BOOLEAN",
    "STMT",
    "OP",
    "OP_REL",
    "OP_LOG",
    "SIGN_REL",
    "SIGN_LOG"
]

GRAMMAR = [
    {
        "development": [
            "PROGRAM"
        ],
        "nonterminal": "S'"
    },
    {
        "development": [
            "main",
            "CMD"
        ],
        "nonterminal": "PROGRAM"
    },
    {
        "development": [
            "LBRACE",
            "EXPR",
            "RBRACE"
        ],
        "nonterminal": "CMD"
    },
    {
        "development": [
            "A"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "B"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "C"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "D"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "E"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "F"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "G"
        ],
        "nonterminal": "EXPR"
    },
    {
        "development": [
            "DECL",
            "G"
        ],
        "nonterminal": "A"
    },
    {
        "development": [
            "IF",
            "G"
        ],
        "nonterminal": "B"
    },
    {
        "development": [
            "WHILE",
            "G"
        ],
        "nonterminal": "C"
    },
    {
        "development": [
            "INPUT",
            "G"
        ],
        "nonterminal": "D"
    },
    {
        "development": [
            "PRINT",
            "G"
        ],
        "nonterminal": "E"
    },
    {
        "development": [
            "ATTR",
            "G"
        ],
        "nonterminal": "F"
    },
    {
        "development": [
            "EXPR"
        ],
        "nonterminal": "G"
    },
    {
        "development": [
            "VOID"
        ],
        "nonterminal": "G",
        "isVoid": True
    },
    {
        "development": [
            "TIPO",
            "VAR",
            "SEMICOLON"
        ],
        "nonterminal": "DECL"
    },
    {
        "development": [
            "TIPO",
            "ATTR"
        ],
        "nonterminal": "DECL"
    },
    {
        "development": [
            "if",
            "LPAR",
            "STMT",
            "RPAR",
            "CMD"
        ],
        "nonterminal": "IF"
    },
    {
        "development": [
            "if",
            "LPAR",
            "STMT",
            "RPAR",
            "CMD",
            "ELSE"
        ],
        "nonterminal": "IF"
    },
    {
        "development": [
            "else",
            "CMD"
        ],
        "nonterminal": "ELSE"
    },
    {
        "development": [
            "VAR",
            "SET",
            "EXPR_AR",
            "SEMICOLON"
        ],
        "nonterminal": "ATTR"
    },
    {
        "development": [
            "EXPR_AR",
            "+",
            "AUX_AR"
        ],
        "nonterminal": "EXPR_AR"
    },
    {
        "development": [
            "EXPR_AR",
            "-",
            "AUX_AR"
        ],
        "nonterminal": "EXPR_AR"
    },
    {
        "development": [
            "AUX_AR"
        ],
        "nonterminal": "EXPR_AR"
    },
    {
        "development": [
            "AUX_AR",
            "*",
            "AUX_AR_F"
        ],
        "nonterminal": "AUX_AR"
    },
    {
        "development": [
            "AUX_AR_F",
            "/",
            "AUX_AR"
        ],
        "nonterminal": "AUX_AR"
    },
    {
        "development": [
            "AUX_AR_F"
        ],
        "nonterminal": "AUX_AR"
    },
    {
        "development": [
            "LPAR",
            "EXPR_AR",
            "RPAR"
        ],
        "nonterminal": "AUX_AR_F"
    },
    {
        "development": [
            "VAR"
        ],
        "nonterminal": "AUX_AR_F"
    },
    {
        "development": [
            "INTEGER"
        ],
        "nonterminal": "AUX_AR_F"
    },
    {
        "development": [
            "FLOAT_N"
        ],
        "nonterminal": "AUX_AR_F"
    },
    {
        "development": [
            "BOOLEAN"
        ],
        "nonterminal": "AUX_AR_F"
    },
    {
        "development": [
            "while",
            "LPAR",
            "STMT",
            "RPAR",
            "CMD"
        ],
        "nonterminal": "WHILE"
    },
    {
        "development": [
            "input",
            "LPAR",
            "VAR",
            "RPAR",
            "SEMICOLON"
        ],
        "nonterminal": "INPUT"
    },
    {
        "development": [
            "print",
            "LPAR",
            "VAR",
            "RPAR",
            "SEMICOLON"
        ],
        "nonterminal": "PRINT"
    },
    {
        "development": [
            ";"
        ],
        "nonterminal": "SEMICOLON"
    },
    {
        "development": [
            "var"
        ],
        "nonterminal": "VAR"
    },
    {
        "development": [
            "="
        ],
        "nonterminal": "SET"
    },
    {
        "development": [
            "int"
        ],
        "nonterminal": "TIPO"
    },
    {
        "development": [
            "float"
        ],
        "nonterminal": "TIPO"
    },
    {
        "development": [
            "bool"
        ],
        "nonterminal": "TIPO"
    },
    {
        "development": [
            "}"
        ],
        "nonterminal": "RBRACE"
    },
    {
        "development": [
            "{"
        ],
        "nonterminal": "LBRACE"
    },
    {
        "development": [
            "("
        ],
        "nonterminal": "LPAR"
    },
    {
        "development": [
            ")"
        ],
        "nonterminal": "RPAR"
    },
    {
        "development": [
            "1"
        ],
        "nonterminal": "INTEGER"
    },
    {
        "development": [
            "1.2"
        ],
        "nonterminal": "FLOAT_N"
    },
    {
        "development": [
            "True"
        ],
        "nonterminal": "BOOLEAN"
    },
    {
        "development": [
            "False"
        ],
        "nonterminal": "BOOLEAN"
    },
    {
        "development": [
            "BOOLEAN"
        ],
        "nonterminal": "STMT"
    },
    {
        "development": [
            "VAR"
        ],
        "nonterminal": "STMT"
    },
    {
        "development": [
            "OP"
        ],
        "nonterminal": "STMT"
    },
    {
        "development": [
            "OP_REL"
        ],
        "nonterminal": "OP"
    },
    {
        "development": [
            "OP_LOG"
        ],
        "nonterminal": "OP"
    },
    {
        "development": [
            "STMT",
            "SIGN_REL",
            "STMT"
        ],
        "nonterminal": "OP_REL"
    },
    {
        "development": [
            "STMT",
            "SIGN_LOG",
            "STMT"
        ],
        "nonterminal": "OP_LOG"
    },
    {
        "development": [
            "=="
        ],
        "nonterminal": "SIGN_REL"
    },
    {
        "development": [
            ">="
        ],
        "nonterminal": "SIGN_REL"
    },
    {
        "development": [
            "<="
        ],
        "nonterminal": "SIGN_REL"
    },
    {
        "development": [
            ">"
        ],
        "nonterminal": "SIGN_REL"
    },
    {
        "development": [
            "<"
        ],
        "nonterminal": "SIGN_REL"
    },
    {
        "development": [
            "and"
        ],
        "nonterminal": "SIGN_LOG"
    },
    {
        "development": [
            "or"
        ],
        "nonterminal": "SIGN_LOG"
    },
    {
        "development": [
            "!"
        ],
        "nonterminal": "SIGN_LOG"
    }
]
