import checkers
def game():
    howbig = int(input("How big would you like your checkerboard? Enter an integer between 4 and 16: "))
    while howbig <= 4 or howbig >= 16:
        howbig = int(input(f'{howbig} is not a valid input. Please enter a value between 4 and 16: '))

    board = checkers.build_board(howbig)

    black_count = checkers.get_count(board, 'Black')
    red_count = checkers.get_count(board, 'Red')
    empty_count = checkers.get_count(board, 'Empty')

    print(board)
    print(f"Black pieces: {black_count}")
    print(f"Red pieces: {red_count}")
    print(f"Empty spaces: {empty_count}")

if __name__ == "__main__":
    game()
