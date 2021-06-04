''' Exhaustive Solve for Cryptarithmetic Puzzles'''


def read_puzzle_from_str(puzzle_str: str):
    '''Reads and transfers given puzzels into divided strings
    >>> a = 'HARD + WORK = MONEY\n
             WORK + WORK = MONEY'
    >>> read_puzzle_from_str(a)
    [(['HARD', 'WORK'], 'MONEY'), (['WORK', 'WORK'], 'MONEY')
    '''
    result = []
    # givide string that has many thumbs
    for thumb in puzzle_str.split('\n'):
        # clean results
        adders, add_result = thumb.split('=')
        adders = [word.strip() for word in adders.split('+')]
        add_result = add_result.strip()
        # give them
        result.append((adders, add_result))
    return result


def read_puzzle_from_file(path: str):
    '''Reads thumbs from file to a list.
       Every new thumb must be written in the new row.'''
    # open file that has many thumbs
    with open(path, r) as file:
        thumbs = file.readlines()
        result = []

        for thumb in thumbs:
            # clean results
            adders, add_result = thumb.split('=')
            adders = [word.strip() for word in adders.split('+')]
            add_result = add_result.strip()
            # give them
            result += (adders, add_result)
    return result


def letters_to_assign(adders: list, add_result: str):
    '''Finds all unique letters needed to assign
    >>> letters_to_assign(['HARD', 'WORK'], 'MONEY')
    ['H', 'A', 'R', 'D', 'W', 'O', 'K', 'M', 'N', 'E', 'Y']
    '''
    all_letters = []
    for word in adders + [add_result]:
        for char in word:
            if char not in all_letters:
                all_letters.append(char)
    return all_letters


def check_solved_puzzle(adders: list, add_result: str, result_dict: dict):
    '''Checks if the result combination from the dict is suitable'''

    adders = [to_digit(word, result_dict) for word in adders]
    add_result = to_digit(add_result, result_dict)
    return sum(adders) == add_result


def to_digit(word: str, result_dict: dict):
    '''Translate a word into a digit
    >>> res_dict = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
    >>> to_digit('abcd', res_dict)
    1234
    '''
    result = [result_dict[char] for char in word]
    return int(''.join(result))


def exostive_solve(adders: list, add_result: str):
    '''Cryptarithmetic solver. Checks every possible combination for the thumb.'''

    # set prequirement arguments
    starting_letters = {word[0] for word in adders} | set(add_result[0])
    letters_left = letters_to_assign(adders, add_result)

    if len(letters_left) > 10:
        print(
            f'Unvalid thumb {adders, add_result}: number of unique letters > 10')

    digits_left = [num for num in '9876543210']
    res_dict = {letter: None for letter in letters_left}
    res_dict['iterations'] = 0

    def exostive_solve_req(letters_left, digits_left):
        '''Help function iters through all the combinations'''
        # if there no digits to assign, it check if correct
        
        if letters_left == []:
            if check_solved_puzzle(adders, add_result, res_dict):
                # hurray! it's a victory!
                print(res_dict)
            return False

        # try all digits that left
        for idx in range(len(digits_left)):
            digit = digits_left[idx]
            char = letters_left[0]

            # starting letters can't be zero
            if (digit == '0') and (char in starting_letters):
                continue
            
            # recurs through all variants
            res_dict[char] = digit
            new_digits_left = digits_left[:idx] + digits_left[idx + 1:]

            exostive_solve_req(letters_left[1:], new_digits_left)
            res_dict[char] = None
            res_dict['iterations'] += 1

        return False

    exostive_solve_req(letters_left, digits_left)
    print(res_dict)


def main(info_type: int, info_sourse: str):
    '''Here you can choose a type of information that you give to the programme: str or file
    You can give more then one thumb at once in the next format:
    'HI + DONE = NEXT\n GIVE + SOME + MONEY = SHOPS'''

    # Chose the format of information
    if info_type == 0:
        all_thumbs = read_puzzle_from_str(info_sourse)
    elif info_type == 1:
        all_thumbs = read_puzzle_from_file(info_sourse)
    else:
        print('Please enter a valid info_type: 0 - for strind, 1 - for file')
        return

    # iter through all thumbs
    for thumb in all_thumbs:
        print()
        adders, add_result = thumb[0], thumb[1]
        exostive_solve(adders, add_result)
