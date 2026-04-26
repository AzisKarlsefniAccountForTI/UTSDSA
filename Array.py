itemgame = ["sword", "shield", "potion", "armor", "ring"]

def lihatitem():
    print("\n=== DAFTAR ITEM ===")
    if len(itemgame) == 0:
        print("Belum ada item")
    else:
        no = 1
        for item in itemgame:
            print(f"{no}. {item}")
            no += 1

def tambahitem():
    nama = input("Nama item: ")
    posisi = int(input("Masukkan posisi (mulai dari 1): "))
    
    if posisi >= 1 and posisi <= len(itemgame) + 1:
        itemgame.insert(posisi - 1, nama)
        print("Item berhasil ditambahkan")
    else:
        print("Posisi tidak valid")

def hapusitem():
    posisi = int(input("Masukkan nomor item yang dihapus: "))
    
    if posisi >= 1 and posisi <= len(itemgame):
        itemgame.pop(posisi - 1)
        print("Item berhasil dihapus")
    else:
        print("Posisi tidak valid")

while True:
    print("\n" + "=" * 10 + " INVENTORY ITEM GAME " + "=" * 10)
    print("1. Lihat Item")
    print("2. Tambah Item")
    print("3. Hapus Item")
    print("0. Keluar")
    
    pilih = input("Pilih: ")

    if pilih == "1":
        lihatitem()
    elif pilih == "2":
        tambahitem()
    elif pilih == "3":
        hapusitem()
    elif pilih == "0":
        break
    else:
        print("Input salah")