import json
import re

from values import TERMINALS, NON_TERMINALS, GRAMMAR

IS_INTEGER = r'\d(\d)*'
IS_FLOAT = r'\d(\d)*\.\d(\d)*'


class SyntaticAnalyser:
    table = {}

    stack = []
    input = []
    actions = []

    def __init__(self):
        self.load_json()

    def analyse(self, tokens):
        self.sanitize_tokens(tokens)

        self.input.append('$')
        self.stack.append('0')

        print("INPUT")
        print(self.input)
        print("\n")

        while True:
            current_input = self.input[0]
            current_stack = int(self.stack[-1])

            table_line = self.table.get(current_input, None)

            if table_line is None:
                if(re.findall(IS_FLOAT, current_input)):
                    table_line = self.table.get('FLOAT_NUM')
                elif(re.findall(IS_INTEGER, current_input)):
                    table_line = self.table.get('INTEGER_NUM')
                else:
                    table_line = self.table.get('VARIABLE_NAME')

            action = table_line[current_stack]

            if "e" in action:
                print('Error')
                break

            if action == 'acc':
                print('Accepted')
                break

            self.actions.append(action)

            operation = action[0]
            next_action = action[1:]

            if operation == 's':
                self.input.pop(0)

                self.stack.append(current_input)
                self.stack.append(next_action)
            elif operation == 'r':
                reduce_rule = GRAMMAR[int(next_action)]

                reduce_char_size = 0 if reduce_rule.get(
                    "isVoid", False) else len(reduce_rule["development"]) * 2

                if reduce_char_size:
                    self.stack = self.stack[:-reduce_char_size]

                goto_state = self.lookup_goto(
                    int(self.stack[-1]), reduce_rule["nonterminal"])

                self.stack.append(reduce_rule["nonterminal"])
                self.stack.append(str(goto_state))

            else:
                print('Error')

    def lookup_goto(self, index, symbol):
        return self.table[symbol][index]

    def sanitize_tokens(self, tokens):
        for token, lexeme, row, col in tokens:
            self.input.append(lexeme)

    def load_json(self):
        f = open('table.json', 'r')

        table = json.load(f)

        f.close()

        self.table = table
        return table
