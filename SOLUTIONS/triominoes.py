import random
import copy
import time

MOD = 1000000007

possible_moves = [
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0)],
    [(1, 1), (0, 1), (1, 0)],
    [(0, 0), (1, 0), (0, 1)]
]


def naive_check_if_complete(board):
    for i in board:
        for j in i:
            if j == -1:
                return False
    return True


def naive_check_if_move_is_feasible(board, move_ind, i, j):
    for (x, y) in possible_moves[move_ind]:
        ti = x + i
        tj = y + j
        if ti < 0 or ti >= len(board) or tj < 0 or tj >= len(board[ti]) or board[ti][tj] != -1:
            return False
    return True


def naive_solve(board, vis):
    board_tpl = tuple(map(tuple, board))
    if board_tpl in vis:
        return 0
    vis.add(board_tpl)
    if naive_check_if_complete(board):
        return 1
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[i])):

            for move_ind in range(len(possible_moves)):
                if not naive_check_if_move_is_feasible(board, move_ind, i, j):
                    continue
                board_cpy = copy.deepcopy(board)
                for (x, y) in possible_moves[move_ind]:
                    ti = x + i
                    tj = y + j
                    board_cpy[ti][tj] = move_ind

                ans += naive_solve(board_cpy, vis)
    return ans


def naive_sol(n, m):
    board = [[-1 for i in range(m)] for i in range(n)]
    return naive_solve(board, set())


def check_if_move_is_feasible(board, n, m, move, ind, j):
    for (x, y) in move:
        ti = x
        tj = y + j
        if ti < 0 or ti + ind >= n or tj < 0 or tj >= m:
            return False
        if board[ti] & (1 << tj):
            return False
    return True


def generate_different_combinations(vis_combinations, curr_board, n, m, ind, j):
    h = (tuple(curr_board), j)
    if h in vis_combinations:
        return vis_combinations[h]

    combinations = []

    if j == m:
        if all((curr_board[0] & (1 << j)) != 0 for j in range(m)):
            return [tuple(curr_board[1:])]
        return []

    combinations.extend(generate_different_combinations(
        vis_combinations, curr_board.copy(), n, m, ind, j + 1))

    for move in possible_moves:
        if not check_if_move_is_feasible(curr_board, n, m, move, ind, j):
            continue
        board_cpy = curr_board.copy()
        for (x, y) in move:
            ti = x
            tj = y + j
            board_cpy[ti] |= (1 << tj)
        combinations.extend(generate_different_combinations(
            vis_combinations, board_cpy, n, m, ind, j + 1))

    vis_combinations[h] = combinations

    return combinations


def solve(n, m, curr_board, ind, vis_boards, vis_combinations):
    """
    By generating states row by row, then only the next two rows could be affected,
    making use of this fact, we store all the possible states and process them
    only once (dynamic programming approach).
    It is very important to note that the number of columns should be the min of n and m.


    Args:
        n (int):
            Number of rows
        m (int):
            Number of columns
        curr_board ([int]):
            represents what hasn't been processed of the board yet.
            each row is represented as an int and using bitmasks to access it,
            this makes is much faster and more memory efficient.
        ind (int):
            the current processed index
        vis_boards ({([int], int) => int}):
            saves number of ways to reach a solution from current board configuration
            state: (2 rows starting from index, index) => int
        vis_combinations ({[int] => [[int]]}):
            saves the possible combinations from each configuration
            state: (board): [board_combination]

    Returns:
        Number of possible full board configurations % MOD
    """

    h = (curr_board[:2], ind)
    if h in vis_boards:
        return vis_boards[h]

    if ind == n:
        return 1

    ans = 0

    for combination in generate_different_combinations(vis_combinations, list(curr_board[: 3]), n, m, ind, 0):
        ans += solve(n, m, combination +
                     curr_board[3:], ind + 1, vis_boards, vis_combinations)
        ans %= MOD

    vis_boards[h] = ans
    return ans


def efficient_sol(n, m):
    n, m = max(n, m), min(n, m)
    board = tuple(0 for i in range(n))
    vis_boards = dict()
    vis_combinations = dict()
    return solve(n, m, board, 0, vis_boards, vis_combinations)


def test_validity(cases_cnt):
    print("Check validity against a slow naive solution for",
          cases_cnt, "random test cases.")
    test_cases = [(2, 8)] + [(random.randint(2, 3), random.randint(3, 6))
                             for i in range(cases_cnt)]
    for n, m in test_cases:
        naive = naive_sol(n, m)
        efficient = efficient_sol(n, m)
        if naive != efficient:
            print("Mismatch at input:", n, m)
            print("The naive_sol is    :", naive)
            print("The efficient sol is:", efficient)
    print("Done")


def benchmark(cases_cnt):
    print("Benchmarking the solution against", cases_cnt, "big inputs.")
    test_cases = [(6, 21)] + [(random.randint(3, 6),
                               random.randint(10, 21)) for i in range(cases_cnt)]
    total_time = 0
    min_time = 1e6
    max_time = 0
    for n, m in test_cases:
        start_time = time.time()
        ans = efficient_sol(n, m)
        elapsed_time = time.time() - start_time
        total_time += elapsed_time
        min_time = min(min_time, elapsed_time)
        max_time = max(max_time, elapsed_time)
    print("Average time taken per input:",
          total_time / len(test_cases), "seconds")
    print("Min time taken:", min_time, "seconds")
    print("Max time taken:", max_time, "seconds")

test_validity(25)
benchmark(100)
