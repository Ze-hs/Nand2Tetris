class Code:
    dest_code = ['null', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    jump_code = ['null', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
    control_table = {
        '0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000',
        '!D':'0001101', '!A':'0110001', '-D':'0001111', '-A':'0110011', 'D+1':'0011111',
        'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011',
        'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001',
        '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011',
        'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'
    }

    def int_to_binary(self, value, precision):
        int_value = int(value)
        return format(int_value, f'0>{precision}b')

    def comp(self, value):
        return self.control_table[value]

    def dest(self, value):
        temp = self.dest_code.index(value)
        return self.int_to_binary(temp, 3)

    def jump(self, value):
        temp = self.jump_code.index(value)
        return self.int_to_binary(temp, 3)

    def get_a_instructions(self, value):
        return self.int_to_binary(value, 16)
