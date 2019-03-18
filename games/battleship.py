from random import randint

for i in range(200):

    board = []

    for x in range(5):
        board.append(["O"] * 5)

    def print_board(game):
        for row in game:
            print(" ".join(row))

    print("There is a battleship somewhere in the ocean. Can you find it within 10 guesses?")
    print_board(board)


    def game_over():
        print("Game Over")
        print("The battleship was here:")
        board[ship_row-1][ship_col-1] = "B"
        print_board(board)

    def random_row(game):
        return randint(0, len(game) - 1)

    def random_col(game):
        return randint(0, len(game[0]) - 1)

    ship_row = random_row(board)+1
    ship_col = random_col(board)+1

    turn = 0
    for each in range(10):
        turn = turn + 1
        print("Turn ", turn)
        is_row = input("Guess Row: ")
        is_col = input("Guess Col: ")

        def test_int(row, col):
            try:
                int(row) and int(col)
                return True
            except ValueError:
                return False

        if not test_int(is_row, is_col):
            print("Please input integer only.")
            if turn == 10:
                game_over()
        else:
            guess_row = int(is_row)
            guess_col = int(is_col)
            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break
            else:
                if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                    print("Oops, that's not even in the ocean.")
                    if turn == 10:
                        game_over()
                elif board[guess_row - 1][guess_col - 1] == "X":
                    print("You guessed that one already.")
                    if turn == 10:
                        game_over()
                else:
                    print("You missed my battleship!")
                    board[guess_row-1][guess_col-1] = "X"
                    print_board(board)
                    if turn == 10:
                        game_over()

    again = input("Do you want to play again?(y/n)")
    while again != "y" and again != "n":
        print("Please input y or n.")
        again = input("Do you want to play again?(y/n)")
    else:
        if again == "y":
            print("Here we go!")
        elif again == "n":
            print("Exiting...")
            break
