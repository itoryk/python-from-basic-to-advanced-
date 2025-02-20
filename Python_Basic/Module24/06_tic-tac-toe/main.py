class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                print(f"Игрок {self.current_player} победил!")
                return True
            elif ' ' not in self.board:
                return True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Неверный ход!")
        return False

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return True
        return False


def play_game():
    game = TicTacToe()
    game_over = False

    while not game_over:
        position = int(input("Выберите позицию для хода (от 0 до 8): "))
        game_over = game.make_move(position)
        game.print_board()


play_game()
