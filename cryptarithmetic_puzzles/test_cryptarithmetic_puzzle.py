from cryptarithmetic_puzzle import *


a = 'HORN + WORK = MONEY'
print(read_puzzle_from_str(a))

a, b = read_puzzle_from_str(a)[0]
puzzle = Croypto_Pyzzle(a, b)
print(puzzle.letters_left)

puzzle.result_dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
print(puzzle.to_digit('abcdcba'))

import time

now= time.time()
exostive_solve(a, b)
print(time.time() - now)

# test_string = '''SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+THEY
# +MAY+SOON+TRY+TO+STAY+AT+HOME+SO+AS+TO+SEE+OR+HEAR+THE+SAME
# +ONE+MAN+TRY+TO+MEET+THE+TEAM+ON+THE+MOON+AS+HE+HAS+AT+THE
# +OTHER+TEN=TESTS'''
# test_string = ''.join(line.strip() for line in test_string.split('\n'))

now= time.time()
main(0, test_string)
b = '''AADF + SFDAGFS = SDFS
        SDFG + SDFGHJ=ZZZZZZZ
        FFFF+HHHHHH = KKKKKKK'''
print(time.time() - now)
