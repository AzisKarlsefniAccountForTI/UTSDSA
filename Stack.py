stackAktivitas = []

def pushAktivitas():
    aksi = input("Masukkan aktivitas player: ")
    stackAktivitas.append(aksi)
    print("Aktivitas berhasil ditambahkan")

def tampilkan():
    if stackAktivitas:
        for i in range(len(stackAktivitas)):
            print(f"{i+1}. {stackAktivitas[i]}")
    else:
        print("Tidak ada aktivitas")

def popAktivitas():
    print("\nSebelum undo:")
    tampilkan()

    if stackAktivitas:
        hapus = stackAktivitas.pop()
        print("\nUndo aktivitas:", hapus)
    else:
        print("\nTidak ada aktivitas yang bisa di-undo")

    print("\nSesudah undo:")
    tampilkan()

while True:
    print("\n" + "=" * 10 + " MENU STACK " + "=" * 10)
    print("1. Push Aktivitas")
    print("2. Undo (Pop)")
    print("3. Lihat Aktivitas")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        pushAktivitas()
    elif pilih == "2":
        popAktivitas()
    elif pilih == "3":
        tampilkan()
    elif pilih == "0":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")