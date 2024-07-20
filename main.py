import tkinter as tk
from tkinter import ttk, messagebox, font
from tkcalendar import DateEntry
from binary_search import binary_search_peminjaman
from sort_functions import bubble_sort_peminjaman, merge_sort_peminjaman

class PeminjamanBarangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Peminjaman Barang")
        
        # custom untuk fontnya
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.entry_font = font.Font(family="Helvetica", size=12)
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        
        self.items = []

        # frame inputan
        self.frame_input = tk.Frame(self.root, bg="lightblue")
        self.frame_input.pack(pady=10)

        # kolom inputan nama barang
        self.label_nama = tk.Label(self.frame_input, text="Nama Barang:", font=self.label_font, bg="lightblue")
        self.label_nama.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nama = tk.Entry(self.frame_input, font=self.entry_font)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)

        # kolom inputan nama peminjam
        self.label_peminjam = tk.Label(self.frame_input, text="Nama Peminjam:", font=self.label_font, bg="lightblue")
        self.label_peminjam.grid(row=1, column=0, padx=5, pady=5)
        self.entry_peminjam = tk.Entry(self.frame_input, font=self.entry_font)
        self.entry_peminjam.grid(row=1, column=1, padx=5, pady=5)

        # kolom inputan tanggal pinjam
        self.label_tanggal_pinjam = tk.Label(self.frame_input, text="Tanggal Pinjam:", font=self.label_font, bg="lightblue")
        self.label_tanggal_pinjam.grid(row=2, column=0, padx=5, pady=5)
        self.entry_tanggal_pinjam = DateEntry(self.frame_input, font=self.entry_font, date_pattern='dd/mm/yyyy')
        self.entry_tanggal_pinjam.grid(row=2, column=1, padx=5, pady=5)

        # kolom inputan tanggal kembali
        self.label_tanggal_kembali = tk.Label(self.frame_input, text="Tanggal Kembali:", font=self.label_font, bg="lightblue")
        self.label_tanggal_kembali.grid(row=3, column=0, padx=5, pady=5)
        self.entry_tanggal_kembali = DateEntry(self.frame_input, font=self.entry_font, date_pattern='dd/mm/yyyy')
        self.entry_tanggal_kembali.grid(row=3, column=1, padx=5, pady=5)

        # tombol tambah peminjaman
        self.button_tambah = tk.Button(self.frame_input, text="Tambah Peminjaman", font=self.button_font, bg="green", fg="white", command=self.tambah_peminjaman)
        self.button_tambah.grid(row=4, columnspan=2, pady=10)

        # frame pencarian
        self.frame_search = tk.Frame(self.root, bg="lightgreen")
        self.frame_search.pack(pady=10)

        # kolom inputan nama peminjam untuk pencarian
        self.label_search = tk.Label(self.frame_search, text="Cari Nama Peminjam:", font=self.label_font, bg="lightgreen")
        self.label_search.grid(row=0, column=0, padx=5, pady=5)
        self.entry_search = tk.Entry(self.frame_search, font=self.entry_font)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5)

        # tombol pencarian
        self.button_search = tk.Button(self.frame_search, text="Cari Peminjaman", font=self.button_font, bg="blue", fg="white", command=self.cari_peminjaman)
        self.button_search.grid(row=1, columnspan=2, pady=10)

        # frame untuk pengurutan
        self.frame_sort = tk.Frame(self.root, bg="lightyellow")
        self.frame_sort.pack(pady=10)

        # pliihan kriteria pengurutan
        self.sort_criteria = tk.StringVar()
        self.sort_criteria.set("Nama Barang")
        self.option_menu = tk.OptionMenu(self.frame_sort, self.sort_criteria, "Nama Barang", "Nama Peminjam", "Tanggal Pinjam", "Tanggal Kembali")
        self.option_menu.grid(row=0, column=0, padx=5, pady=5)

        # plihan urutan pengurutan
        self.sort_order = tk.StringVar()
        self.sort_order.set("ASC")
        self.order_menu = tk.OptionMenu(self.frame_sort, self.sort_order, "ASC", "DESC")
        self.order_menu.grid(row=0, column=1, padx=5, pady=5)

        # tombol bubble sort
        self.button_bubble_sort = tk.Button(self.frame_sort, text="Bubble Sort", font=self.button_font, bg="purple", fg="white", command=self.bubble_sort)
        self.button_bubble_sort.grid(row=0, column=2, padx=5, pady=5)

        # tombol merge sort
        self.button_merge_sort = tk.Button(self.frame_sort, text="Merge Sort", font=self.button_font, bg="brown", fg="white", command=self.merge_sort)
        self.button_merge_sort.grid(row=0, column=3, padx=5, pady=5)

        # frame list peminjaman
        self.frame_list = tk.Frame(self.root, bg="lightgray")
        self.frame_list.pack(pady=10)

        # table list peminjaman
        self.tree = ttk.Treeview(self.frame_list, columns=("Nama Barang", "Nama Peminjam", "Tanggal Pinjam", "Tanggal Kembali"), show='headings')
        self.tree.heading("Nama Barang", text="Nama Barang")
        self.tree.heading("Nama Peminjam", text="Nama Peminjam")
        self.tree.heading("Tanggal Pinjam", text="Tanggal Pinjam")
        self.tree.heading("Tanggal Kembali", text="Tanggal Kembali")
        self.tree.column("Nama Barang", width=150)
        self.tree.column("Nama Peminjam", width=150)
        self.tree.column("Tanggal Pinjam", width=100)
        self.tree.column("Tanggal Kembali", width=100)
        self.tree.pack(side=tk.LEFT, padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(self.frame_list, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # tombol hapus
        self.button_hapus = tk.Button(self.root, text="Hapus Peminjaman", font=self.button_font, bg="red", fg="white", command=self.hapus_peminjaman)
        self.button_hapus.pack(pady=10)

    def tambah_peminjaman(self):
        nama_barang = self.entry_nama.get()
        nama_peminjam = self.entry_peminjam.get()
        tanggal_pinjam = self.entry_tanggal_pinjam.get()
        tanggal_kembali = self.entry_tanggal_kembali.get()

        if nama_barang and nama_peminjam and tanggal_pinjam and tanggal_kembali:
            peminjaman = (nama_barang, nama_peminjam, tanggal_pinjam, tanggal_kembali)
            self.items.append(peminjaman)
            self.tree.insert('', tk.END, values=peminjaman)

            self.entry_nama.delete(0, tk.END)
            self.entry_peminjam.delete(0, tk.END)
            self.entry_tanggal_pinjam.set_date('')
            self.entry_tanggal_kembali.set_date('')
        else:
            messagebox.showwarning("Input Salah", "Mohon isi semua bidang.")

    def hapus_peminjaman(self):
        selected_item = self.tree.selection()

        if selected_item:
            self.tree.delete(selected_item)
            for item in selected_item:
                self.items.remove(self.tree.item(item, "values"))
        else:
            messagebox.showwarning("Tidak Ada Pilihan", "Pilih item yang ingin dihapus.")

    def cari_peminjaman(self):
        nama_peminjam = self.entry_search.get()
        if nama_peminjam:
            result = binary_search_peminjaman(self.items, nama_peminjam)
            if result != -1:
                messagebox.showinfo("Peminjaman Ditemukan", f"Peminjaman ditemukan:\n{result}")
            else:
                messagebox.showinfo("Peminjaman Tidak Ditemukan", "Peminjaman tidak ditemukan.")
        else:
            messagebox.showwarning("Input Salah", "Mohon isi nama peminjam untuk mencari.")

    def bubble_sort(self):
        kriteria = self.sort_criteria.get()
        order = self.sort_order.get()
        self.items = bubble_sort_peminjaman(self.items, kriteria, order)
        self.update_treeview()

    def merge_sort(self):
        kriteria = self.sort_criteria.get()
        order = self.sort_order.get()
        self.items = merge_sort_peminjaman(self.items, kriteria, order)
        self.update_treeview()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.items:
            self.tree.insert('', tk.END, values=item)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeminjamanBarangApp(root)
    root.mainloop()
