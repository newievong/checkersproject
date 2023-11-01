from numpy import random, ndarray
def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], (size, size))
    return board

def get_count(board, status):
    count = (board == status).sum()
    return count


if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")