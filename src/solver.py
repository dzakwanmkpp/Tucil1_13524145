import os
import time

def solve_queens(board, live=True, delay=0.2, callback=None):
    n = len(board)

    checked = 0
    start = time.time()

    update_interval = 1 if n <= 5 else 20 if n <= 7 else 5000

    config = [0] * n
    selesai = False
    while not selesai:

        checked += 1

        if callback and checked % update_interval == 0:
            callback(list(config), checked)

        if live and checked % update_interval == 0:
            temp = [row[:] for row in board]

            for r in range(n):
                c = config[r]
                temp[r][c] = '#'

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Mencoba konfigurasi ke-{checked}\n")

            for row in temp:
                print("".join(row))
            time.sleep(delay)

        if is_valid_config(board, config):
            solution = [row[:] for row in board]
            for r in range(n):
                solution[r][config[r]] = '#'
            elapsed = (time.time() - start) * 1000

            if live:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Solusi ditemukan:\n")
                for row in solution:
                    print("".join(row))
            return solution, checked, elapsed

        i = n - 1
        while i >= 0:
            config[i] += 1
            if config[i] < n:
                break
            config[i] = 0
            i -= 1
        if i < 0:
            selesai = True

    elapsed = (time.time() - start) * 1000
    return None, checked, elapsed

def validate_board(board):
    if not board: 
        return False

    n = len(board)

    for row in board:
        if len(row) != n:
            return False

    regions = set()
    for row in board:
        for cell in row:
            if not ('A' <= cell <= 'Z'):
                return False
            regions.add(cell)

    if len(regions) != n:
        return False
    return True

def is_valid_config(board, queen):
    n = len(board)

    if len(set(queen)) != n:
        return False

    used_regions = set()
    for r in range(n):
        region = board[r][queen[r]]
        if region in used_regions:
            return False
        used_regions.add(region)

    for r1 in range(n):
        c1 = queen[r1]
        for r2 in range(r1 + 1, n):
            c2 = queen[r2]
            if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
                return False
    return True

