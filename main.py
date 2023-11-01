def game():
    import checkers

    howbig = int(input("How big would you like your checkerboard? Enter an integer between 4 and 16: "))
    board = checkers.build_board(howbig)

    black_count = checkers.get_count(board, 'Black')
    red_count = checkers.get_count(board, 'Red')
    empty_count = checkers.get_count(board, 'Empty')

    print(f"Black pieces: {black_count}")
    print(f"Red pieces: {red_count}")
    print(f"Empty spaces: {empty_count}")

if __name__ == "__main__":
    game()