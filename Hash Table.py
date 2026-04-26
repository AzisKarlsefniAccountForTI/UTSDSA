size = 5
hashtable = [[] for _ in range(size)]

def hashfungsi(iduser):
    return iduser % size

def tambahdata():
    iduser = input("Masukkan ID (5 digit): ")

    if not iduser.isdigit() or len(iduser) != 5:
        print("ID harus berupa 5 digit angka!")
        return

    iduser = int(iduser)
    nama = input("Masukkan nama: ")

    index = hashfungsi(iduser)

    if hashtable[index]:
        print("Terjadi collision di index", index)

    hashtable[index].append((iduser, nama))
    print("Data ditambahkan")

def caridata():
    iduser = input("Masukkan ID yang dicari (5 digit): ")

    if not iduser.isdigit() or len(iduser) != 5:
        print("ID harus berupa 5 digit angka!")
        return

    iduser = int(iduser)
    index = hashfungsi(iduser)

    for data in hashtable[index]:
        if data[0] == iduser:
            print(f"Data ditemukan -> ID: {data[0]} | Nama: {data[1]}")
            return

    print("Data tidak ditemukan")

def lihatdata():
    print("\n" + "=" * 10 + " DATA HASH TABLE " + "=" * 10)
    
    for i in range(size):
        print(f"\nIndex {i}")
        print("  ID     | Nama")
        print("  --------------")

        if hashtable[i]:
            for data in hashtable[i]:
                print(f"  {data[0]:<6} | {data[1]}")
        else:
            print("  - kosong -")

while True:
    print("\n" + "=" * 10 + " HASH TABLE USER " + "=" * 10)
    print("1. Tambah Data")
    print("2. Cari Data")
    print("3. Lihat Data")
    print("0. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        tambahdata()
    elif pilih == "2":
        caridata()
    elif pilih == "3":
        lihatdata()
    elif pilih == "0":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")