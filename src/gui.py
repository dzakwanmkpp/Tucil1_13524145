import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
import os
from solver import solve_queens, validate_board

LIST_WARNA = [
    '#FFB374', '#7AB8F5', '#A8D8A8', '#F07070', '#C8A8E8',
    '#F0E070', '#B0B0B0', '#D4A878', '#70D0D0', '#F0A0C8',
    '#A0C8F0', '#C8F0A0', '#F0C8A0'
]

class QueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Queens Puzzle Solver")
        self.root.resizable(False, False)

        self.board = None
        self.solusi = None
        self.sedang_solve = False
        self.skip = False

        frame_atas = tk.Frame(root, padx=10, pady=10)
        frame_atas.pack()

        self.btn_buka = tk.Button(frame_atas, text="Pilih File", command=self.buka_file, width=12)
        self.btn_buka.grid(row=0, column=0, padx=5)

        self.btn_solve = tk.Button(frame_atas, text="Solve", command=self.jalankan_solve, width=12, state=tk.DISABLED)
        self.btn_solve.grid(row=0, column=1, padx=5)

        self.btn_simpan = tk.Button(frame_atas, text="Simpan", command=self.simpan_solusi, width=12, state=tk.DISABLED)
        self.btn_simpan.grid(row=0, column=2, padx=5)

        self.btn_skip = tk.Button(frame_atas, text="Skip", command=self.skip_animasi, width=12, state=tk.DISABLED)
        self.btn_skip.grid(row=0, column=3, padx=5)

        frame_delay = tk.Frame(root, padx=10)
        frame_delay.pack()
        tk.Label(frame_delay, text="Delay (detik):").grid(row=0, column=0)
        self.entry_delay = tk.Entry(frame_delay, width=8)
        self.entry_delay.insert(0, "0.1")
        self.entry_delay.grid(row=0, column=1, padx=5)

        self.label_file = tk.Label(root, text="Belum ada file dipilih", fg="gray")
        self.label_file.pack(pady=(5, 0))

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.label_info = tk.Label(root, text="", font=("Arial", 10))
        self.label_info.pack(pady=(0, 10))

    def buka_file(self):
        if self.sedang_solve:
            return
        path = filedialog.askopenfilename(
            title="Pilih file board",
            filetypes=[("Text files", "*.txt")]
        )
        if not path:
            return

        board = []
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    board.append(list(line))

        if not validate_board(board):
            messagebox.showerror("Error", "Board tidak valid!")
            return

        self.board = board
        self.solusi = None
        self.btn_solve.config(state=tk.NORMAL)
        self.btn_simpan.config(state=tk.DISABLED)
        self.label_info.config(text="")

        nama = os.path.basename(path)
        self.label_file.config(text=f"File: {nama}", fg="black")

        huruf_ada = sorted(set(h for row in board for h in row))
        self.warna_map = {}
        for i, h in enumerate(huruf_ada):
            self.warna_map[h] = LIST_WARNA[i % len(LIST_WARNA)]

        self.gambar_board(self.board)

    def gambar_board(self, board, queen_pos=None):
        self.canvas.delete("all")
        n = len(board)

        ukuran = min(400, 60 * n)
        self.canvas.config(width=ukuran, height=ukuran)
        cell = ukuran // n

        font_crown = max(10, cell // 2)

        for baris in range(n):
            for kolom in range(n):
                x1 = kolom * cell
                y1 = baris * cell
                x2 = x1 + cell
                y2 = y1 + cell

                huruf = board[baris][kolom]
                warna = self.warna_map.get(huruf, '#DDDDDD')

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=warna, outline="black", width=2)

                if queen_pos and queen_pos[baris] == kolom:
                    cx = x1 + cell // 2
                    cy = y1 + cell // 2
                    self.canvas.create_text(cx, cy, text="♛", font=("Arial", font_crown))

    def update_progres(self, config, checked):
        if self.skip:
            return
        self.root.after(0, self._gambar_progres, config, checked)
        try:
            delay = float(self.entry_delay.get())
        except ValueError:
            delay = 0.1

        sisa = delay
        while sisa > 0 and not self.skip:
            time.sleep(min(0.05, sisa))
            sisa -= 0.05

    def _gambar_progres(self, config, checked):
        self.gambar_board(self.board, config)
        self.label_info.config(text=f"Mencoba konfigurasi ke-{checked}...")

    def skip_animasi(self):
        self.skip = True
        self.btn_skip.config(state=tk.DISABLED)
        self.label_info.config(text="Skipping animasi, tunggu hasil...")

    def jalankan_solve(self):
        if not self.board or self.sedang_solve:
            return

        self.sedang_solve = True
        self.skip = False
        self.btn_solve.config(state=tk.DISABLED)
        self.btn_buka.config(state=tk.DISABLED)
        self.btn_simpan.config(state=tk.DISABLED)
        self.btn_skip.config(state=tk.NORMAL)
        self.label_info.config(text="Sedang mencari solusi...")

        t = threading.Thread(target=self._solve_thread)
        t.start()

    def _solve_thread(self):
        hasil, checked, waktu = solve_queens(self.board, live=False, callback=self.update_progres)

        self.root.after(0, self._tampilkan_hasil, hasil, checked, waktu)

    def _tampilkan_hasil(self, hasil, checked, waktu):
        self.sedang_solve = False
        self.btn_solve.config(state=tk.NORMAL)
        self.btn_buka.config(state=tk.NORMAL)
        self.btn_skip.config(state=tk.DISABLED)

        if hasil is None:
            self.label_info.config(text=f"Tidak ada solusi. ({checked} kasus, {waktu:.2f} ms)")
            self.solusi = None
            self.btn_simpan.config(state=tk.DISABLED)
            self.gambar_board(self.board)
        else:
            self.solusi = hasil
            self.btn_simpan.config(state=tk.NORMAL)

            queen_pos = []
            for baris in hasil:
                queen_pos.append(baris.index('#'))

            self.gambar_board(self.board, queen_pos)
            self.label_info.config(text=f"Solusi ditemukan! ({checked} kasus, {waktu:.2f} ms)")

    def simpan_solusi(self):
        if not self.solusi:
            return
        path = filedialog.asksaveasfilename(
            title="Simpan solusi",
            filetypes=[("Text files", "*.txt")]
        )
        if path:
            with open(path, "w") as f:
                for row in self.solusi:
                    f.write("".join(row) + "\n")
            messagebox.showinfo("Berhasil", "Solusi berhasil disimpan!")

if __name__ == "__main__":
    root = tk.Tk()
    app = QueensGUI(root)
    root.mainloop()
