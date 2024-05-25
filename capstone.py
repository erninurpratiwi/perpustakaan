# Inisialisasi daftar buku
daftar_buku = {
    1: {'judul': 'Chasing Unicorns', 'penulis': 'Nicko Widjaja', 'tahun': '2023', 'penerbit' : 'Gramedia', 'kategori' : 'Bisnis & Ekonomi', "dipinjam": False},
    2: {'judul': 'Outliers', 'penulis': 'Malcolm Gladwell', 'tahun': '2012', 'penerbit' : 'Sinar star book', 'kategori' : 'Psikologi', "dipinjam": False},
    3: {'judul': 'Atomic Habits', 'penulis': 'James Clear', 'tahun': '2020', 'penerbit' : 'Penguin US', 'kategori' : 'Pengembangan diri', "dipinjam": False},
    4: {'judul': 'Becoming A Sibling', 'penulis': 'Elkey Chereyl', 'tahun': '2023', 'penerbit' : 'Wunderkidd Karya Indonesia', 'kategori' : 'Buku Cerita Anak', "dipinjam": False},
    5: {'judul': 'Gadis Kretek', 'penulis': 'Ratih Kumala', 'tahun': '2012', 'penerbit' : 'Gramedia', 'kategori' : 'Novel Fiksi', "dipinjam": False}
}

daftar_peminjam = {}

# Fungsi untuk menampilkan menu
def menu():
    print("==================PERPUSTAKAAN PURWADHIKA==================")
    print("Pilih daftar menu untuk mengakses program :\n")
    print("1. Lihat Daftar Buku")
    print("2. Cari Buku")
    print("3. Tambah Data Buku")
    print("4. Ubah Data Buku")
    print("5. Hapus Data Buku")
    print("6. Lihat Daftar Peminjam Buku")
    print("7. Tambah Peminjam Buku")
    print("8. Hapus Data Peminjam Buku")
    print("9. Keluar")

# Fungsi untuk menampilkan daftar buku
def lihat_daftar_buku():
    while True:
        print("==================Lihat Daftar Buku==================")
        print("1. Lihat Daftar Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            if not daftar_buku:
                print("Tidak ada buku di perpustakaan.")
                return lihat_daftar_buku()
            else:
                print("="*150)
                print("{:<5} {:<30} {:<25} {:<10} {:<30} {:<30} {:<5}".format('ID', 'Judul', 'Penulis', 'Tahun' , 'Penerbit', 'Kategori', 'Status'))
                print("="*150)
                for id, buku in daftar_buku.items():
                    status = "dipinjam" if buku["dipinjam"] else "tersedia"
                    print("{:<5} {:<30} {:<25} {:<10} {:<30} {:<30} {:<5}".format(id, buku["judul"], buku["penulis"], buku["tahun"], buku["penerbit"], buku["kategori"], status))
                return lihat_daftar_buku()
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi untuk mencari buku berdasarkan judul
def cari_buku():
    while True:
        print("==================Cari Buku==================")
        print("1. Cari Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            found = False
            judul = input("Masukkan judul buku yang ingin dicari: ")
            for id, buku in daftar_buku.items():
                if buku["judul"].lower() == judul.lower():
                    found = True
                    status = "dipinjam" if buku["dipinjam"] else "tersedia"
                    print(f"ID: {id}, Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}, Penerbit: {buku['penerbit']}, Kategori: {buku['kategori']}, Status: {status}")    
                    return cari_buku()
            if not found:
                print(f"Buku dengan judul '{judul}'  tidak ditemukan.")
                return cari_buku()
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi untuk menambahkan buku baru
def tambah_buku():
    while True:
        print("==================Menambahkan Buku Baru==================")
        print("1. Menambahkan Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            id = int(input("Masukkan ID buku baru: "))
            if id in daftar_buku:
                print(f"Buku dengan ID {id} sudah ada.")
                continue
            else:
                judul = input("Masukkan judul buku baru: ")
                penulis = input("Masukkan nama penulis buku: ")
                tahun = int(input("Masukkan tahun terbit: "))
                penerbit = input("Masukkan penerbit: ")
                kategori = input("Masukkan kategori buku: ") 
                while True:
                    konfirmasi = input("Apakah Anda yakin? (ya/tidak): ").lower()
                    if konfirmasi == "ya":
                        daftar_buku[id] = {"judul": judul, "penulis": penulis, "tahun" : tahun, "penerbit": penerbit, "kategori": kategori, "dipinjam": False}
                        print(f"Buku '{judul}' oleh {penulis} telah ditambahkan.")
                        break
                    elif konfirmasi == "tidak":
                        print(f"Buku '{judul}' oleh {penulis} gagal ditambahkan.")
                        return tambah_buku()
                    else:
                        print("Pilihan tidak valid. Mohon masukkan 'ya' atau 'tidak'.")
                return tambah_buku()            
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi untuk memperbarui informasi buku
def ubah_data_buku():
    while True:
        print("==================Memperbarui Informasi Buku==================")
        print("1. Memperbarui Informasi Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            id = int(input("Masukkan ID buku yang ingin diubah: "))
            if id in daftar_buku:
                judul = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
                penulis = input("Masukkan penulis baru (kosongkan jika tidak ingin mengubah): ")
                tahun = input("Masukkan tahun terbit (kosongkan jika tidak ingin mengubah): ")
                penerbit = input("Masukkan penerbit (kosongkan jika tidak ingin mengubah): ")
                kategori = input("Masukkan kategori buku (kosongkan jika tidak ingin mengubah): ")
                while True:
                    konfirmasi = input("Apakah Anda yakin? (ya/tidak): ").lower()
                    if konfirmasi == "ya":
                        if judul:
                            daftar_buku[id]["judul"] = judul
                        if penulis:
                            daftar_buku[id]["penulis"] = penulis
                        if tahun:
                            daftar_buku[id]["tahun"] = tahun
                        if penerbit:
                            daftar_buku[id]["penerbit"] = penerbit
                        if kategori:
                            daftar_buku[id]["kategori"] = kategori
                        print(f"Informasi buku dengan ID {id} telah diperbarui.")
                        break
                    elif konfirmasi == "tidak":
                        print(f"Buku dengan ID {id} gagal diperbarui.")
                        return ubah_data_buku()
                    else:
                        print("Pilihan tidak valid. Mohon masukkan 'ya' atau 'tidak'.")
                return ubah_data_buku()
            else:
                print(f"Buku dengan ID {id} tidak ditemukan.")
                continue
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi untuk menghapus buku dari daftar buku
def hapus_data_buku():
    while True:
        print("==================Menghapus Data Buku==================")
        print("1. Menghapus Data Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            id = int(input("Masukkan ID buku yang ingin dihapus: "))
            if id in daftar_buku:
                while True:
                    konfirmasi = input("Apakah Anda yakin? (ya/tidak): ").lower()
                    if konfirmasi == "ya":
                        del daftar_buku[id]
                        print(f"Buku dengan ID {id} telah dihapus.")
                        break
                    elif konfirmasi == "tidak":
                        print(f"Buku dengan ID {id} tetap tersimpan.")
                        return hapus_data_buku()
                    else:
                        print("Pilihan tidak valid. Mohon masukkan 'ya' atau 'tidak'.")
                return hapus_data_buku()
            else:
                print(f"Buku dengan ID {id} tidak ditemukan.")
                return hapus_data_buku()
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi untuk menampilkan daftar peminjam buku
def lihat_daftar_peminjam():
    while True:
        print("==================Lihat Daftar Peminjam Buku==================")
        print("1. Lihat Daftar Peminjam Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            if not daftar_peminjam:
                print("Tidak ada peminjam buku saat ini.")
                return lihat_daftar_peminjam()
            else:
                print("="*70)
                print("{:<10} {:<20} {:<20}".format('ID Buku', 'Nama Peminjam', 'Tanggal Pinjam'))
                print("="*70)
                for id_buku, data_peminjam in daftar_peminjam.items():
                    print("{:<10} {:<20} {:<20}".format(id_buku, data_peminjam["nama"], data_peminjam["tanggal_pinjam"]))
                continue
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")
 
# Fungsi untuk menambahkan peminjam buku
def tambah_peminjam():
    while True:
        print("==================Menambahkan Peminjam Buku==================")
        print("1. Menambahkan Peminjam Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            id_buku = int(input("Masukkan ID buku yang ingin dipinjam: "))
            if id_buku in daftar_buku:
                if not daftar_buku[id_buku]["dipinjam"]:
                    nama_peminjam = input("Masukkan nama peminjam: ")
                    tanggal_pinjam = input("Masukkan tanggal peminjaman (DD-MM-YYYY): ")
                    while True: 
                        konfirmasi = input("Apakah Anda yakin? (ya/tidak): ").lower()
                        if konfirmasi == "ya":
                            daftar_buku[id_buku]["dipinjam"] = True
                            daftar_peminjam[id_buku] = {"nama": nama_peminjam, "tanggal_pinjam": tanggal_pinjam}
                            print(f"{nama_peminjam} telah meminjam buku dengan ID {id_buku}.")
                            break
                        elif konfirmasi == "tidak":
                            print(f"{nama_peminjam} batal meminjam buku dengan ID {id_buku}.")
                            return tambah_peminjam()
                        else:
                            print("Pilihan tidak valid. Mohon masukkan 'ya' atau 'tidak'.")
                    return tambah_peminjam()
                else:
                    print(f"Buku dengan ID {id_buku} sedang dipinjam oleh orang lain.")
                    return tambah_peminjam()
            else:
                print(f"Buku dengan ID {id_buku} tidak ditemukan.")
                return tambah_peminjam()
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi untuk menghapus data peminjam buku
def hapus_data_peminjam():
    while True:
        print("==================Menghapus Data Peminjam Buku==================")
        print("1. Menghapus Data Peminjam Buku")
        print("2. Kembali ke Menu")
        balik_menu = input("Silahkan Pilih Sub Menu [1-2]: ")
        if balik_menu == '1':
            id_buku = int(input("Masukkan ID buku yang ingin dikembalikan: "))
            if id_buku in daftar_buku:
                if id_buku in daftar_peminjam:
                    while True:
                        konfirmasi = input("Apakah Anda yakin? (ya/tidak): ").lower()
                        if konfirmasi == "ya":
                            del daftar_peminjam[id_buku]
                            daftar_buku[id_buku]["dipinjam"] = False
                            print(f"Data peminjam buku dengan ID {id_buku} telah dihapus. Buku telah dikembalikan.")
                            break
                        elif konfirmasi == "tidak":
                            print(f"Data peminjam buku dengan ID {id_buku} batal dihapus.")
                            return hapus_data_peminjam()
                        else:
                            print("Pilihan tidak valid. Mohon masukkan 'ya' atau 'tidak'.")
                    return hapus_data_peminjam()
                else:
                    print(f"Buku dengan ID {id_buku} tidak sedang dipinjam.")
                    return hapus_data_peminjam()
            else:
                print(f"Buku dengan ID {id_buku} tidak ditemukan.")
                return hapus_data_peminjam()
        if balik_menu == '2':
            break
        else: 
            print("Masukkan jawaban yang valid [1-2]")

# Fungsi utama
if __name__ == "__main__":
    while True:
        menu()
        pilihan = input("Masukkan pilihan Anda (1-9): ")

        if pilihan == '1':
            lihat_daftar_buku()
            print("\n") 
        elif pilihan == '2':
            cari_buku()
            print("\n")
        elif pilihan == '3':
            tambah_buku()
            print("\n")
        elif pilihan == '4':
            ubah_data_buku()
            print("\n")
        elif pilihan == '5':
            hapus_data_buku()
            print("\n")
        elif pilihan == '6':
            lihat_daftar_peminjam()
            print("\n")
        elif pilihan == '7':
            tambah_peminjam()
            print("\n")
        elif pilihan == '8':
            hapus_data_peminjam()
            print("\n")
        elif pilihan == '9':
            print("Terima kasih telah menggunakan layanan perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan (1-9).")