"""this module creates board and fills it with words using backtracking"""

class Crosssword:
    """
    create board and fill it with letters
    """
    def __init__(self, size, path):
        """
        initlize variables
        """
        # self.board = [["" for _ in range(size[1])] for _ in range(size[0])]

        # for 5x4 board
        # self.board = [["z", "y", "m", "e"], 
        #               ["y", "o", "u", "l"], 
        #               ["g", "u", "r", "u"], 
        #               ["a", "v", "i", "d"],
        #               ["l", "e", "", ""]]

        # for 3x4 board
        self.board = [['s', 'o', 'r', 'a'],
                      ['a', 'l', 'a', 's'],
                      ['a', 'm', '', '']]

        self.size = size
        self.list = []
        self.row_list = []
        self.col_list = []
        self.path = path

    def word_lists(self):
        """
        create lists that contain only words of certain length
        """
        file = open(self.path)
        lst = file.readlines()
        self.row_list = list(filter(lambda x: len(x[:-1]) == self.size[1], lst))
        self.col_list = list(filter(lambda x: len(x[:-1]) == self.size[0], lst))
  
    def clear(self, position):
        """
        remove letter at a certain position
        """
        self.board[position[0]][position[1]] = ""
    
    def first_empty_place(self):
        """
        find the first empty space
        """
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.board[i][j] == "":
                    return (i, j)
                else: continue

    def best_match(self, prime_word, lst):
        """
        get dictionary with letters as keys and
        amount of words that can be created with them
        """
        dictionary = dict()
        for letter in range(97, 123):
            new_lst = list(filter(lambda x: prime_word + chr(letter) == x[:len(prime_word) + 1], lst))
            dictionary[chr(letter)] = len(new_lst)
        
        return dictionary
    
    def get_dict(self):
        """
        check is it is possible to create wirds in columns and rows;
        get list with letters that are sorten in the way that the last
        letter can create the most words and the first the least
        """
        lst = []
        for i in range(self.size[1]):
            word = ""
            for j in range(self.size[0]):
                word += self.board[j][i]

                if word not in lst: 
                    lst.append(word)

        while "" in lst:
            lst.remove("")

        for word in lst:
            l = list(filter(lambda x: word == x[:len(word)], self.col_list))
            if l == []:
                return False

        row_lst = []
        for row in self.board:
            s = ""
            row_word = s.join(row)
            if row_word != "":
                row_lst.append(row_word)
            l = list(filter(lambda x: row_word == x[:len(row_word)], self.row_list))
            if l == []:
                return False

        dct = dict()
        if row_lst != []:
            row_word = row_lst[-1]

        for i in range(97, 122):
            dct[chr(i)] = self.best_match(row_word, self.row_list)[chr(i)]

        sorted_dct = {letter: num for letter, num in sorted(dct.items(), key = lambda item: item[1])}

        return [letter for letter in sorted_dct]

    def fill_board(self):
        """
        fill board with letters
        """
        def add_letter(lst, row, col):
            if lst == False:
                if col == 0:
                    row -= 1
                    col = self.size[1] - 1
                else:
                    col -= 1
                self.clear([row, col])
                lst = self.get_dict()
                self.used_letters[row, col] += 1
                for _ in range(self.used_letters[row, col]):
                    if lst == False:
                        return add_letter(lst, row, col)
                    elif lst == []:
                        lst = False
                        return add_letter(lst, row, col)
                    else:
                        lst.pop(-1)
                return add_letter(lst, row, col)
            if lst != []:
                letter = lst[-1]
            else: 
                lst = False
                return add_letter(lst, row, col)
            self.board[row][col] = letter

            for row in self.board:
                print(row)
            print()

        self.word_lists()

        self.used_letters = dict()
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.used_letters[row, col] = 0

        while self.first_empty_place() != None:
            row = self.first_empty_place()[0]
            col = self.first_empty_place()[1]
            self.current_position = [row, col]
            lst = self.get_dict()
            
            add_letter(lst, row, col)
        
        return self.board

if __name__ == '__main__':
    c = Crosssword((3, 4), "/home/master/ucu/semester2/discrete_project/words.txt")
    # c = Crosssword((5, 4), "/home/master/ucu/semester2/discrete_project/words.txt")
    c.word_lists()
    for row in c.fill_board():
        print(row)
