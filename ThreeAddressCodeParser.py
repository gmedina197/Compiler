class ThreeAddressCodeParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.code = []
        self.temp_var_count = 0
        self.L_var_count = 0

    def parse(self):
        for i, token in enumerate(self.tokens):
            type, lexeme, context, row, col = token

            if type in ['INT', 'FLOAT', 'BOOL']:
                self.variable_declaration(i)

            if type in ["IF", "WHILE", "ELSE"]:
                self.block_statements(i)

    def block_statements(self, idx, block_type=None):
        statements = []

        idx += 1
        if block_type == 'IF':
            while self.tokens[idx][0] != 'RBRACKET':
                statements.append(self.tokens[idx][1])
                idx += 1

            l_var = f'L{self.L_var_count}'
            l_next = f'L{self.L_var_count+1}'

            print(statements)
            self.code.append(
                f'{l_var}: if({statements[0]} {statements[1]} {statements[2]}) goto {l_next}')

        while idx < len(self.tokens):
            statements.append(self.tokens[idx])

            if self.tokens[idx][0] == 'IF':
                # +1 because of the IF token
                self.block_statements(idx + 1, 'IF')

            """ if self.tokens[idx][0] == 'RBRACKET':
                break """

            idx += 1

        print(self.code)

    def variable_declaration(self, idx):
        decl = []

        while idx < len(self.tokens):
            decl.append(self.tokens[idx])

            if self.tokens[idx][0] == 'SEMICOLON':
                break

            idx += 1

        n_values = len(list(filter(lambda x: x[0] in [
                       'INTEGER', 'FLOATN', 'BOOLEAN', 'VAR'], decl))) - 1

        if n_values == 0:
            self.code.append(f'{decl[1][1]} = 0')
        elif n_values == 1:
            self.code.append(f'{decl[1][1]} = {decl[3][1]}')
        elif n_values == 2:
            self.code.append(
                f'{decl[1][1]} = {decl[3][1]} {decl[4][1]} {decl[5][1]}')
        else:
            var = decl[1][1]

            decl = decl[3:-1]

            operation = list(map(lambda x: x[1], decl))

            for i in range(n_values-1):
                op_idx = next((idx for idx, x in enumerate(operation) if x in [
                    '*', '/']), next((idx for idx, x in enumerate(operation) if x in ['+', '-']), None))

                self.code.append(
                    f'T{self.temp_var_count} = {operation[op_idx-1]} {operation[op_idx]} {operation[op_idx+1]}')

                operation = operation[:op_idx-1] + \
                    [f'T{self.temp_var_count}'] + operation[op_idx+2:]

                if i != n_values - 2:
                    self.temp_var_count += 1

            self.code.append(f"{var} = {f'T{self.temp_var_count}'}")
            self.temp_var_count += 1
