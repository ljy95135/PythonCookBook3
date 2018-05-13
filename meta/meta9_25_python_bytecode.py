import dis  # Disassembler of Python byte code
import opcode
import types


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')


dis.dis(countdown)
c = countdown.__code__.co_code
print(opcode.opname[c[0]])  # SETUP_LOOP


def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)


for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)


def add(x, y):
    return x + y


c = add.__code__
newbytecode = b'xxxxxxx'
nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount,
                    c.co_nlocals, c.co_stacksize, c.co_flags, newbytecode, c.co_consts,
                    c.co_names, c.co_varnames, c.co_filename, c.co_name,
                    c.co_firstlineno, c.co_lnotab)
add.__code__ = nc
# SystemError: unknown opcode
# add(2, 3)  # Segmentation fault
