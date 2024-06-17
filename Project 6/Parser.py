import Code
import SymbolTable
from pathlib import Path

class Parser:
    def __init__(self, hack_file):
        self.file_name = hack_file.stem
        self.path = hack_file
        self.code = Code.Code()
        self.symbolTable = SymbolTable.SymbolTable()
        self.symbol_counter = 16

    ''' Remove all comments and leading/trailing whitespace'''

    def strip_line(self, line):
        return line.split("//")[0].strip()

    def first_pass(self):
        counter = 0

        # Add all the labels to the symbol table
        with (open(self.path, 'r') as asm_file):
            for line in asm_file:
                clean_line = self.strip_line(line)
                if not clean_line:
                    continue

                if clean_line[0] == '(':
                    self.symbolTable.add(clean_line[1:-1], counter)
                    continue

                counter += 1

    def parse(self, line):
        # label
        if line[0] == '(':
            pass

        # A-instructions
        elif line[0] == '@' and not line[1:].isnumeric():
            if self.symbolTable.contains(line[1:]):
                code = self.symbolTable.get_value(line[1:])
                return self.code.int_to_binary(code, 16)
            
            self.symbolTable.add(line[1:], self.symbol_counter)
            self.symbol_counter += 1
            return self.code.int_to_binary(self.symbolTable.get_value(line[1:]), 16)

        elif line[0] == '@' and line[1:].isnumeric():
            return self.code.int_to_binary(line[1:], 16)

        # C instructions
        else:
            dest = "null"
            jump = "null"

            temp = line.split('=')
            if '=' in line:
                dest = temp[0].strip()

            temp = temp[-1].split(';')
            comp = temp[0].strip()

            if ';' in line:
                jump = temp[1].strip()

            bin_dest = self.code.dest(dest)
            bin_comp = self.code.comp(comp)
            bin_jump = self.code.jump(jump)

            return f'111{bin_comp}{bin_dest}{bin_jump}'

    def run(self):
        # Read file
        self.first_pass()

        output = Path('output') / f'{self.file_name}.hack'
        with open(self.path, 'r') as asm_file, open(output, 'w') as machine_file:
            for line in asm_file:
                clean_line = self.strip_line(line)
                parsed_line = ''

                if clean_line:
                    parsed_line = self.parse(clean_line)

                if parsed_line:
                    machine_file.write(f'{parsed_line}\n')
