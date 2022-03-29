class Field:
    size = [['.' for i in range(3)] for j in range(3)]

    def info(self):
        print('Доска для крестики-нолики:')
        for i in range(len(self.size)):
            for j in range(len(self.size)):
                print(self.size[i][j], end='\t')
            print()

    def crosses(self, x, y):
        for i in range(len(self.size)):
            for j in range(len(self.size)):
                self.size[x][y] = 'X'

    def noughts(self, x, y):
        for i in range(len(self.size)):
            for j in range(len(self.size)):
                self.size[x][y] = 'O'

    def tie(self):
        summa_crosses = 0
        summa_noughts = 0

        for i in range(len(self.size)):
            for j in range(len(self.size)):
                if self.size[i][j] == 'X':
                    summa_crosses += 1
                elif self.size[i][j] == 'O':
                    summa_noughts += 1
        if ((summa_crosses == 3 and summa_noughts == 4)
            or (summa_crosses == 4 and summa_noughts == 3)):
                print('Игра окочена! Ничья!')
                return True
        else:
            return False

    def check_field(self, x, y):
        if self.size[int(x)][int(y)] == '.':
            return True
        else:
            return False

    def win(self):
        for i in range(len(self.size)):
            for j in range(len(self.size)):
                if ((self.size[0][0] == 'X' and self.size[0][1] == 'X' and self.size[0][2] == 'X')
                        or (self.size[1][0] == 'X' and self.size[1][1] == 'X' and self.size[1][2] == 'X')
                        or (self.size[2][0] == 'X' and self.size[2][1] == 'X' and self.size[2][2] == 'X')
                        or (self.size[0][0] == 'X' and self.size[1][0] == 'X' and self.size[2][0] == 'X')
                        or (self.size[0][1] == 'X' and self.size[1][1] == 'X' and self.size[2][1] == 'X')
                        or (self.size[0][2] == 'X' and self.size[1][2] == 'X' and self.size[2][2] == 'X')
                        or (self.size[0][0] == 'X' and self.size[1][1] == 'X' and self.size[2][2] == 'X')
                        or (self.size[0][2] == 'X' and self.size[1][1] == 'X' and self.size[2][0] == 'X')):
                    print('Игра окочена! Победитель Игрок 1!')
                    return True

                elif ((self.size[0][0] == 'O' and self.size[0][1] == 'O' and self.size[0][2] == 'O')
                        or (self.size[1][0] == 'O' and self.size[1][1] == 'O' and self.size[1][2] == 'O')
                        or (self.size[2][0] == 'O' and self.size[2][1] == 'O' and self.size[2][2] == 'O')
                        or (self.size[0][0] == 'O' and self.size[1][0] == 'O' and self.size[2][0] == 'O')
                        or (self.size[0][1] == 'O' and self.size[1][1] == 'O' and self.size[2][1] == 'O')
                        or (self.size[0][2] == 'O' and self.size[1][2] == 'O' and self.size[2][2] == 'O')
                        or (self.size[0][0] == 'O' and self.size[1][1] == 'O' and self.size[2][2] == 'O')
                        or (self.size[0][2] == 'O' and self.size[1][1] == 'O' and self.size[2][0] == 'O')):
                    print('Игра окочена! Победитель Игрок 2!')
                    return True


field = Field()
check_win = True

field.info()
while check_win:

    try:

        choice_1 = input('Игрок 1, Ваш ход: ').split()

        try:

            if field.check_field(int(choice_1[0]), int(choice_1[1])):

                field.crosses(int(choice_1[0]), int(choice_1[1]))

                field.info()

                if field.win():
                    check_win = False

                    break

                elif field.tie() and not field.win():
                    check_win = False
                    break

            else:
                print('Вы не можете ходить в клетку {} {}'.format(int(choice_1[0]), int(choice_1[1])))
                while not field.check_field(int(choice_1[0]), int(choice_1[1])):
                    choice_1 = input('Игрок 1, Ваш ход: ').split()
                field.crosses(int(choice_1[0]), int(choice_1[1]))
                field.info()

        except ValueError:
            print('Введите числа, а не символы или буквы.')
            choice_1 = input('Игрок 1, Ваш ход: ').split()

    except ValueError as e:
        print(e)
        choice_1 = input('Игрок 1, Ваш ход: ').split()

    except IndexError:
        print('Неправильный ввод.')
        choice_1 = input('Игрок 1, Ваш ход: ').split()
    try:
        choice_2 = input('Игрок 2, Ваш ход: ').split()
        try:
            if field.check_field(int(choice_2[0]), int(choice_2[1])):

                field.noughts(int(choice_2[0]), int(choice_2[1]))

                field.info()

                if field.win():
                    check_win = False
                    break

                elif field.tie() and not field.win():

                    check_win = False
                    break

            else:
                print('Вы не можете ходить в клетку {} {}'.format(int(choice_2[0]), int(choice_2[1])))
                while not field.check_field(int(choice_2[0]), int(choice_2[1])):

                    choice_2 = input('Игрок 2, Ваш ход: ').split()
                field.noughts(int(choice_2[0]), int(choice_2[1]))
                field.info()

        except ValueError:
            print('Введите числа, а не символы или буквы.')
            choice_2 = input('Игрок 2, Ваш ход: ').split()

    except ValueError:
        print('Введите числа, а не символы или буквы.')
        choice_2 = input('Игрок 2, Ваш ход: ').split()
    except IndexError:
        print('Неправильный ввод.')
