class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

datauser = linkedlist()

def tambahdata():
    nama = input("Masukkan nama pengguna: ")
    nodebaru = Node(nama)

    if datauser.head is None:
        datauser.head = nodebaru
    else:
        sekarang = datauser.head
        while sekarang.next:
            sekarang = sekarang.next
        sekarang.next = nodebaru

    print("Data ditambahkan")

def hapusdata():
    nama = input("Masukkan nama yang dihapus: ")

    sekarang = datauser.head
    prev = None

    while sekarang:
        if sekarang.nama == nama:
            if prev is None:
                datauser.head = sekarang.next
            else:
                prev.next = sekarang.next
            print("Data dihapus")
            return
        prev = sekarang
        sekarang = sekarang.next

    print("Data tidak ditemukan")

def lihatdata():
    print("Data pengguna:")
    sekarang = datauser.head

    if sekarang is None:
        print("Data kosong")
    else:
        no = 1
        while sekarang:
            print(f"{no}. {sekarang.nama}")
            sekarang = sekarang.next
            no += 1

while True:
    print("\n" + "=" * 10 + " LINKED LIST USER " + "=" * 10)
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Lihat Data")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambahdata()
    elif pilih == "2":
        hapusdata()
    elif pilih == "3":
        lihatdata()
    elif pilih == "0":
        break
    else:
        print("Pilihan tidak valid")