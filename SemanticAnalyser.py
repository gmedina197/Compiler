from tokenize import group
from SemanticException import SemanticException
from itertools import groupby

EQUIVALENCY_MAP = {
    'INTEGER': 'INT',
    'FLOATN': 'FLOAT',
    'BOOLEAN': 'BOOL'
}


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


class SemanticAnalyser:
    def __init__(self):
        self.symbol_table = {}
        self.tokens = []

    #(token, lexeme, row, col)
    def analyse(self, tokens):
        self.tokens = tokens

        self.get_tokens_context()

        self.build_symbol_table()

        self.validate_attrs()

        self.validate_statements()

        self.check_unused_vars()

    def check_unused_vars(self):
        for key in self.symbol_table.keys():
            var_name = key.split('-')[0]

            unused = list(
                filter(lambda x: x[0] == 'VAR' and x[1] == var_name, self.tokens))

            if len(unused) == 1:
                print(
                    f'WARNING: Variable {var_name} is declared but not used at line {unused[0][2]} and column {unused[0][3]}')

    def validate_statements(self):
        for index, token in enumerate(self.tokens):
            if(token[0] == 'IF' or token[0] == 'WHILE'):
                ops = []
                idx = index + 2
                token_aux = self.tokens[idx]
                while token_aux[0] != 'RBRACKET':
                    ops.append(token_aux)
                    idx += 1
                    token_aux = self.tokens[idx]

                self.validate_statement_expression(ops)

    def validate_statement_expression(self, ops):
        op_types = []
        for index, op in enumerate(ops):
            if(op[0] == 'VAR'):
                type = self.symbol_table[f'{op[1]}-{op[4]}']['value_type']
                op_types.append(type)
            elif(op[0] in ['INTEGER', 'FLOATN', 'BOOLEAN']):
                op_types.append(op[0])
            elif(op[0] not in ['EQ', 'LE', 'GE', 'LT', 'GT', 'OR', 'AND']):
                raise SemanticException(
                    f'Operator {op[0]} is not supported', op)

        if(not all_equal(op_types)):
            raise SemanticException(
                f'Operators are not of the same type', ops[0])

        print(op_types)

    def get_tokens_context(self):
        context = 0
        context_stack = [1]

        for index, token in enumerate(self.tokens):
            if(token[0] == 'LBRACE'):
                context += 1
                context_stack.append(context)

            self.tokens[index] = token + (context_stack[-1],)

            if(token[0] == 'RBRACE'):
                context_stack.pop()

    def validate_attrs(self):
        for index, token in enumerate(self.tokens):
            type = token[0]

            if(type == 'ATTR'):
                id_token = self.tokens[index - 1]

                exists = [val for key, val in self.symbol_table.items()
                          if id_token[1] in key]

                var_context = id_token[4]
                decl_context = exists[0]['context']

                if not exists or decl_context > var_context:
                    raise Exception(
                        f'Variable {id_token[1]} does not exist')

                ops = []
                token_aux = self.tokens[index + 1]
                while token_aux[0] != 'SEMICOLON':
                    ops.append(token_aux)
                    index += 1
                    token_aux = self.tokens[index + 1]

                self.verify_attr_value(
                    f'{id_token[1]}-{decl_context}', id_token, ops)

    def verify_attr_value(self, symbol_key, id, ops):
        symbol_info = self.symbol_table[symbol_key]

        for index, op in enumerate(ops):
            attr_type = EQUIVALENCY_MAP.get(ops[index][0], None)
            var_type = symbol_info['type']

            if(not attr_type):
                if(ops[index][0] == 'VAR'):
                    next_id = ops[index]

                    if symbol_info['context'] > next_id[4]:
                        raise SemanticException(
                            f'Variable {next_id[1]} is not in the same context as {symbol_key}', next_id)

                    elif(not self.symbol_table.get(f'{next_id[1]}-{symbol_info["context"]}', None)):
                        raise SemanticException(
                            f'Variable {next_id[1]} does not exist', next_id)

                    # elif(id[4] != self.symbol_table[f'{next_id[1]}-{next_id[4]}'][2]):
                elif(ops[index][0] != 'VAR' and ops[index][0] not in ['PLUS', 'MINUS', 'MULT', 'DIV']):
                    raise SemanticException(
                        f'Operator {ops[index][0]} is not supported', ops[index])

                continue

            is_valid = attr_type == var_type
            if not is_valid:
                raise SemanticException(
                    f'Variable {symbol_key} is of type {var_type}, but {attr_type} is found', id)

    def build_symbol_table(self):
        for index, token in enumerate(self.tokens):
            type = token[0]

            if (type in ['INT', 'FLOAT', 'BOOL']):
                next_token = self.tokens[index + 1]

                exists = self.symbol_table.get(
                    f'{next_token[1]}-{next_token[4]}', None)

                if exists:
                    raise SemanticException(
                        f'Variable {next_token[1]} already exists', next_token)

                EQUIVALENCY_MAP = {
                    'INT': 'INTEGER',
                    'FLOAT': 'FLOATN',
                    'BOOL': 'BOOLEAN'
                }

                self.symbol_table[f'{next_token[1]}-{next_token[4]}'] = {
                    'type': token[0],
                    'context': next_token[4],
                    'value_type': EQUIVALENCY_MAP[token[0]],
                    'row': next_token[2],
                    'col': next_token[3]
                }
