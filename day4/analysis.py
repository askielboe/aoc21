import numpy as np

numbers = np.loadtxt("numbers.txt", delimiter=',')
boards = np.loadtxt("boards.txt").reshape(100, 5, 5)

# Question 1
markers = np.zeros(boards.shape, dtype=bool)
for n in numbers:
    markers += boards == n
    if 1 in np.prod(markers, axis=2):
        # winning row
        winning_axis = 2
        break
    if 1 in np.prod(markers, axis=1):
        # winning column
        winning_axis = 1
        break

print("WINNER!")
print("number: ", n)
loc = np.where(np.prod(markers, axis=winning_axis) == 1)
winning_board = boards[loc[0]]
winning_row = boards[loc]
unmarked_on_winner = winning_board[~markers[loc[0]]]

print("winning board:\n", winning_board)
print("winning row: ", winning_row)

print("result: ", int(np.sum(unmarked_on_winner) * n))

# Question 2
boards = np.loadtxt("boards.txt").reshape(100, 5, 5)
winning_axis = None
markers = np.zeros(boards.shape, dtype=bool)
for n in numbers:
    markers += boards == n
    if 1 in np.prod(markers, axis=2):
        # last board to win
        winning_axis = 2
    if 1 in np.prod(markers, axis=1):
        # winning column
        winning_axis = 1

    if winning_axis is not None:
        loc = np.where(np.prod(markers, axis=winning_axis) == 1)
        winning_board = boards[loc[0]]
        winning_row = boards[loc]
        unmarked_on_winner = winning_board[~markers[loc[0]]]

        print("WINNER! removing board: ", loc[0], "len boards = ", len(boards))

        if len(boards) == 3:
            print(boards)
            print(markers)

        boards = np.delete(boards, loc[0], axis=0)
        markers = np.delete(markers, loc[0], axis=0)

        if len(boards) == 0:
            break

        # print("winning board:\n", winning_board)
        # print("winning row: ", winning_row)

    winning_axis = None

print("result: ", int(np.sum(unmarked_on_winner) * n))
