import tkinter as tk
from tkinter import ttk

def f(x, func):
    return eval(func)

def bisection_method(func, a, b, Epsilon):
    iterasi = [(a, b)]
    while (b - a) > Epsilon:
        c = (a + b) / 2

        if f(c, func) == 0.0:
            return c, iterasi

        if f(a, func) * f(c, func) < 0:
            b = c
        else:
            a = c
        
        iterasi.append((a, b))

    c = (a + b) / 2
    return c, iterasi

class BisectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Bisection")

        self.label_func = tk.Label(self.root, text="Masukkan fungsi / f(x) (contoh: x**2 - 4):")
        self.label_func.pack()
        self.entry_func = tk.Entry(self.root)
        self.entry_func.pack()

        self.label_a = tk.Label(self.root, text="Nilai a:")
        self.label_a.pack()
        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack()

        self.label_b = tk.Label(self.root, text="Nilai b:")
        self.label_b.pack()
        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack()

        self.label_epsilon = tk.Label(self.root, text="Toleransi (Epsilon / e):")
        self.label_epsilon.pack()
        self.entry_epsilon = tk.Entry(self.root)
        self.entry_epsilon.pack()

        self.calculate_button = tk.Button(self.root, text="Hitung Akar", command=self.calculate_root)
        self.calculate_button.pack()
        
        self.tree = ttk.Treeview(self.root, columns=("a_value", "b_value", "c_value"))
        self.tree.heading("#0", text="Iterasi")
        self.tree.heading("a_value", text="Nilai a")
        self.tree.heading("b_value", text="Nilai b")
        self.tree.heading("c_value", text="Nilai c")
        self.tree.pack()
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.iteration_label = tk.Label(self.root, text="")
        self.iteration_label.pack()

    def calculate_root(self):
        func_input = self.entry_func.get()
        a_input = self.entry_a.get()
        b_input = self.entry_b.get()
        epsilon_input = self.entry_epsilon.get()

        if not all([func_input, a_input, b_input, epsilon_input]):
            self.result_label.config(text="Error: Semua Kolom harus diisi")
            return

        try:
            a = float(a_input)
            b = float(b_input)
            epsilon = float(epsilon_input)
        except ValueError:
            self.result_label.config(text="Error: Masukkan angka yang valid")
            return

        result, iterasi = bisection_method(func_input, a, b, epsilon)

        if iterasi:
            self.display_iteration(iterasi)
            self.result_label.config(text=f"Akar dari fungsi adalah: {result}")
            self.iteration_label.config(text=f"Akar ditemukan pada iterasi ke-{len(iterasi) - 1}")
        else:
            self.result_label.config(text="Error: Tidak dapat menemukan akar")

    def display_iteration(self, iterasi):
        # Hapus semua entri dalam Treeview sebelum menambahkan data baru
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Tambahkan iterasi yang baru ke dalam tabel
        for i, (a_val, b_val) in enumerate(iterasi):
            c_val = (a_val + b_val) / 2  # Hitung nilai c
            self.tree.insert("", "end", text=f"Iterasi ke-{i}", values=(a_val, b_val, c_val))  # Masukkan nilai c ke dalam tabel

if __name__ == "__main__":
    root = tk.Tk()
    app = BisectionGUI(root)
    root.mainloop()
