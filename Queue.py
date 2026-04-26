from collections import deque

antrianuser = deque()

def enqueue():
    nama = input("Masukkan nama pengguna: ")
    antrianuser.append(nama)
    print("Pengguna masuk antrian")

def tampilkan():
    if antrianuser:
        for i in range(len(antrianuser)):
            print(f"{i+1}. {antrianuser[i]}")
    else:
        print("Antrian kosong")

def dequeue():
    print("\nSebelum diproses:")
    tampilkan()

    if antrianuser:
        nama = antrianuser.popleft()
        print("\nPengguna dilayani:", nama)
    else:
        print("\nTidak ada antrian")

    print("\nSesudah diproses:")
    tampilkan()

while True:
    print("\n" + "=" * 10 + " ANTRIAN LAYANAN " + "=" * 10)
    print("1. Tambah Antrian (Enqueue)")
    print("2. Proses Layanan (Dequeue)")
    print("3. Lihat Antrian")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        enqueue()
    elif pilih == "2":
        dequeue()
    elif pilih == "3":
        tampilkan()
    elif pilih == "0":
        break
    else:
        print("Pilihan tidak valid")