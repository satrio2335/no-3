class AntrianRestoran:
    def _init_(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if len(self.antrian) > 0:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' telah dihapus dari antrian.")
            return pesanan
        else:
            print("Antrian kosong, tidak ada pesanan yang dihapus.")
            return None

    def tampilkan_antrian(self):
        if len(self.antrian) > 0:
            print("Daftar antrian pesanan:")
            for i, pesanan in enumerate(self.antrian, start=1):
                print(f"{i}. {pesanan}")
        else:
            print("Antrian kosong.")

# Contoh penggunaan
antrian = AntrianRestoran()

# Menambahkan pesanan ke dalam antrian
antrian.enqueue("Nasi Goreng")
antrian.enqueue("Ayam Bakar")
antrian.enqueue("Sate Kambing")

# Menampilkan antrian
antrian.tampilkan_antrian()

# Menghapus pesanan dari antrian
antrian.dequeue()
antrian.dequeue()

# Menampilkan antrian setelah menghapus pesanan
antrian.tampilkan_antrian()

# Menghapus pesanan terakhir dari antrian
antrian.dequeue()

# Menampilkan antrian setelah semua pesanan dihapus
antrian.tampilkan_antrian()

# Mencoba menghapus dari antrian kosong
antrian.dequeue()