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
            "MAIN",
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
            "IFNT",
            "G"
        ],
        "nonterminal": "B"
    },
    {
        "development": [
            "WHILENT",
            "G"
        ],
        "nonterminal": "C"
    },
    {
        "development": [
            "INPUTNT",
            "G"
        ],
        "nonterminal": "D"
    },
    {
        "development": [
            "PRINTNT",
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
        "nonterminal": "G"
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
            "IF",
            "LPAR",
            "STMT",
            "RPAR",
            "CMD"
        ],
        "nonterminal": "IFNT"
    },
    {
        "development": [
            "IF",
            "LPAR",
            "STMT",
            "RPAR",
            "CMD",
            "ELSENT"
        ],
        "nonterminal": "IFNT"
    },
    {
        "development": [
            "ELSE",
            "CMD"
        ],
        "nonterminal": "ELSENT"
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
            "WHILE",
            "LPAR",
            "STMT",
            "RPAR",
            "CMD"
        ],
        "nonterminal": "WHILENT"
    },
    {
        "development": [
            "INPUT",
            "LPAR",
            "VAR",
            "RPAR",
            "SEMICOLON"
        ],
        "nonterminal": "INPUTNT"
    },
    {
        "development": [
            "PRINT",
            "LPAR",
            "VAR",
            "RPAR",
            "SEMICOLON"
        ],
        "nonterminal": "PRINTNT"
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
            "INT"
        ],
        "nonterminal": "TIPO"
    },
    {
        "development": [
            "FLOAT"
        ],
        "nonterminal": "TIPO"
    },
    {
        "development": [
            "BOOL"
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
            "int_num"
        ],
        "nonterminal": "INTEGER"
    },
    {
        "development": [
            "float_num"
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
            "INTEGER"
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
            "AND"
        ],
        "nonterminal": "SIGN_LOG"
    },
    {
        "development": [
            "OR"
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