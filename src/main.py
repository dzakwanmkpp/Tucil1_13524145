import os
from solver import solve_queens, validate_board

def read_board(filename):
    if not os.path.exists(filename):
        filename = os.path.join("..", "test", filename)
    board = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                board.append(list(line))
    return board

def print_board(board):
    for row in board:
        print("".join(row))

def save_solution(filename, board):
    with open(filename, "w") as f:
        for row in board:
            f.write("".join(row) + "\n")

def main():
    filename = input("Masukkan nama file: ").strip()

    try:
        board = read_board(filename)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    if not validate_board(board):
        print("\nBoard tidak valid.")
        return

    print("\nMode pencarian:")
    print("1. Langsung solusi (tanpa animasi)")
    print("2. Live condition (dengan animasi)")
    pilihan = input("Pilih mode (1/2): ").strip()

    if pilihan == "2":
        delay_input = input("Masukkan delay (detik, contoh: 0.2): ").strip()
        try:
            delay = float(delay_input)
        except ValueError:
            delay = 0.2
        live = True
    else:
        live = False
        delay = 0

    print("\nBoard input:")
    print_board(board)
    
    solution, checked, elapsed = solve_queens(board, live=live, delay=delay)

    if solution is None:
        print("\nTidak ada solusi.")
    else:
        print("\nSolusi ditemukan:")
        print_board(solution)

    print(f"\nWaktu pencarian: {elapsed:.2f} ms")
    print(f"Banyak kasus yang ditinjau: {checked} kasus")

    simpan = input("Apakah Anda ingin menyimpan solusi? (Ya/Tidak): ")
    if simpan.lower() == "ya" and solution:
        outname = input("Nama file output: ")
        save_solution(outname, solution)
        print("Solusi disimpan.")

if __name__ == "__main__":
    main()



