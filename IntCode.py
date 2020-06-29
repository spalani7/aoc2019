
class IntCodeProgram:
    def __init__(self, code):
        self.code = list(code) # copy program
        self.relative_base_offset = 0
        self.input_list = []
        self.output_list = []

    def set_mem(self, opcode, mode, index, val):
        if mode == 0: # position mode
            self.check_extend_mem(index)
            self.code[ index ] = val
        elif mode == 2: # relative mode
            self.check_extend_mem(self.relative_base_offset + index)
            self.code[ self.relative_base_offset + index ] = val
        elif mode == 1: # immediate mode
            print("Mode not supported for output")
        
    def check_extend_mem(self, index):
        if index < 0:
            print('NEGATIVE MEMORY ADDRESS')
        elif index >= len(self.code):
    #         print('Extending list from {} to {}'.format(len(code), index+1))
            self.code += [0 for x in range(0, (index-len(self.code)+1))] # extending memory
    
    def eval_params(self, opcode, param1, param2):
        try:
            if int(opcode[-3]) == 0: # position mode
                self.check_extend_mem(param1)
                val1 = self.code[ param1 ]
            elif int(opcode[-3]) == 1: # immediate mode
                val1 = param1
            elif int(opcode[-3]) == 2: # relative mode
                self.check_extend_mem(self.relative_base_offset + param1)
                val1 = self.code[ self.relative_base_offset + param1 ]
        except IndexError:
            print('Index_error')
            val1 = 0

        if param2 is not None:
            try:
                if int(opcode[-4]) == 0: # position mode
                    self.check_extend_mem(param2)
                    val2 = self.code[ param2 ]
                elif int(opcode[-4]) == 1: # immediate mode
                    val2 = param2
                elif int(opcode[-4]) == 2: # relative mode
                    self.check_extend_mem(self.relative_base_offset + param2)
                    val2 = self.code[ self.relative_base_offset + param2 ]
            except IndexError:
                print('Index_error')
                val2 = 0
        else:
            val2 = None
        return (val1, val2)


    def run(self):
        j = 0 # program counter
        while True:
            opcode = '{:06d}'.format(self.code[j])
    #         print(opcode, j)
            if int(opcode[-2:]) == 1: # add
                val1, val2 = self.eval_params(opcode, self.code[j+1], self.code[j+2] )
                self.set_mem(opcode, int(opcode[-5]), self.code[j+3], val1 + val2)
        #         print(input_list)
                j += 4
            elif int(opcode[-2:]) == 2: # multiply
                val1, val2 = self.eval_params(opcode, self.code[j+1], self.code[j+2] )
                self.set_mem(opcode, int(opcode[-5]), self.code[j+3], val1 * val2)
        #         print(input_list)
                j += 4
            elif int(opcode[-2:]) == 3: # store
                while len(self.input_list) == 0:
                    pass
#                 print('\nConsuming : {}'.format(self.input_list[0]))
                store_in = int(input()) if len(self.input_list) == 0 else int(self.input_list.pop(0))
    #             print(j, relative_base_offset, opcode, code[j+1], store_in)
                self.set_mem(opcode, int(opcode[-3]), self.code[j+1], store_in)
                j += 2
            elif int(opcode[-2:]) == 4: # load
                val1, _ = self.eval_params(opcode, self.code[j+1], None )
                self.output_list.append(val1)
    #             print(val1)
                j += 2
            elif int(opcode[-2:]) == 5: # jump if true
                val1, val2 = self.eval_params(opcode, self.code[j+1], self.code[j+2] )
                if val1 != 0:
                    if val2 >= len(self.code):
                        print("JUMPING TO LA LA LAND")
    #                 print("Jumping to {}".format(val2))
                    j = val2
                else:
                    j += 3
            elif int(opcode[-2:]) == 6: # jump if false
                val1, val2 = self.eval_params(opcode, self.code[j+1], self.code[j+2] )
                if val1 == 0:
                    if val2 >= len(self.code):
                        print("JUMPING TO LA LA LAND")
    #                 print("Jumping to {}".format(val2))
                    j = val2
                else:
                    j += 3
            elif int(opcode[-2:]) == 7: # less than 
                val1, val2 = self.eval_params(opcode, self.code[j+1], self.code[j+2] )
                if val1 < val2:
                    self.set_mem(opcode, int(opcode[-5]), self.code[j+3], 1)
                else:
                    self.set_mem(opcode, int(opcode[-5]), self.code[j+3], 0)
                j += 4
            elif int(opcode[-2:]) == 8: # equal
                val1, val2 = self.eval_params(opcode, self.code[j+1], self.code[j+2] )
                if val1 == val2:
                    self.set_mem(opcode, int(opcode[-5]), self.code[j+3], 1)
                else:
                    self.set_mem(opcode, int(opcode[-5]), self.code[j+3], 0)
                j += 4
            elif int(opcode[-2:]) == 9: # change relative base_offset
                val1, _ = self.eval_params(opcode, self.code[j+1], None )
                self.relative_base_offset += val1
                j += 2
            elif int(opcode[-2:]) == 99 or j >= len(self.code):
                self.output_list.append('HALT')
                break
            else:
                print("unknown opcode {:06d}@{}".format(code[j], j))