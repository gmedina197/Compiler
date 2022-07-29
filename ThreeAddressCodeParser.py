from multiprocessing import current_process
import re

RELOP_MAPPING = {
    '<': '>=',
    '>': '<=',
    '<=': '>',
    '>=': '<',
    '==': '!=',
}

class ThreeAddressCodeParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.code = []
        self.temp_var_count = 0
        self.L_var_count = 0
        self.labels = []

    def parse(self):
        i = 0
        """ operation = list(map(lambda x: x[0], self.tokens))
        print(operation) """

        current_block = ['MAIN']
        while i < len(self.tokens):
            token = self.tokens[i]

            type = token[0]

            if type in ['INT', 'FLOAT', 'BOOL']:
                idx = self.variable_declaration(i, is_declaration=True)
                i = idx

            if type == 'VAR':
                idx = self.variable_declaration(i, is_declaration=False)
                i = idx

            if type in ["IF", "WHILE", "ELSE"]:
                current_block.append(type)
                idx = self.block_statements(i, block_type=type)
                i = idx

            if type == 'INPUT':
                self.code.append(f'INPUT {self.tokens[i + 2][1]}')
                i += 3

            if type == 'PRINT':
                self.code.append(f'PRINT {self.tokens[i + 2][1]}')
                i += 3

            if type == 'RBRACE' and len(current_block) > 1:
                if(current_block.pop() in ['WHILE']):
                    self.code.append(self.labels.pop())

                self.code.append(self.labels.pop())

            i += 1

        self.print_3_addr_code()

    def print_3_addr_code(self):
        for line in self.code:
            if(not re.match(r'^L\d+', line)):
                print('  ' + line)
            else:
                print(line)

    def block_statements(self, idx, block_type=None):
        statements = []

        current_context = self.tokens[idx][4]

        l_var = f'L{self.L_var_count}'

        if (block_type == 'WHILE'):
            idx += 2
            while self.tokens[idx][0] != 'RBRACKET':
                statements.append(self.tokens[idx][1])
                idx += 1

            l_next = f'L{self.L_var_count + 1}'
            self.code.append(f'{l_var}:')
            self.code.append(
                f'IF {statements[0]} {RELOP_MAPPING[statements[1]]} {statements[2]} goto {l_next}')

            self.labels.append(f'{l_next}:')
            self.labels.append(f'goto {l_var}')

            self.L_var_count += 2

        if block_type == 'IF':
            idx += 2
            while self.tokens[idx][0] != 'RBRACKET':
                statements.append(self.tokens[idx][1])
                idx += 1

            self.code.append(
                f'IF {statements[0]} {RELOP_MAPPING[statements[1]]} {statements[2]} goto {l_var}'
            )

            self.labels.append(f'{l_var}:')
            self.L_var_count += 1

        if block_type == 'ELSE':
            i = len(self.code) - 1
            found = 0
            while i >= 0:
                if 'IF' in self.code[i]:
                    found += 1

                if found == current_context + 1:
                    break

                i -= 1

            label_index = self.code.index(self.code[i][-2:] + ':')

            self.code.insert(label_index, f'goto {l_var}')

            l_next = f'L{self.L_var_count + 1}'

            self.labels.append(f'{l_var}:')

            self.L_var_count += 1

        return idx

    def variable_declaration(self, idx, is_declaration=True):
        decl = []

        while idx < len(self.tokens):
            decl.append(self.tokens[idx])

            if self.tokens[idx][0] == 'SEMICOLON':
                break

            idx += 1

        n_values = len(list(filter(lambda x: x[0] in [
                       'INTEGER', 'FLOATN', 'BOOLEAN', 'VAR'], decl))) - 1

        var = decl[1][1] if is_declaration else decl[0][1]

        if is_declaration:
            decl = decl[3:-1]
        else:
            decl = decl[2:-1]

        if n_values == 0:
            self.code.append(f'{var} = 0')
        elif n_values == 1:
            self.code.append(f'{var} = {decl[0][1]}')
        elif n_values == 2:
            self.code.append(
                f'{var} = {decl[0][1]} {decl[1][1]} {decl[2][1]}')
        else:

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

        return idx
