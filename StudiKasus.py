from collections import deque

# HASH TABLE
dataplayer = {}

# QUEUE
antriandungeon = deque()

# STACK
riwayatdungeon = []

# ARRAY
logaktivitas = []

def tampiljudul():
    print("""
        
 ⡏⢱ ⡇⢸ ⡷⣸ ⡎⠑ ⣏⡉ ⡎⢱ ⡷⣸   ⣇⣸ ⣏⡉ ⣏⡱ ⡎⢱
 ⠧⠜ ⠣⠜ ⠇⠹ ⠣⠝ ⠧⠤ ⠣⠜ ⠇⠹   ⠇⠸ ⠧⠤ ⠇⠱ ⠣⠜
""")

def tambahdata():
    nama = input("Masukkan nama player: ")

    if nama in dataplayer:
        print("Player sudah ada")
        return

    dataplayer[nama] = "idle"
    riwayatdungeon.append("daftar " + nama)
    logaktivitas.append("daftar " + nama)

    print("Player ditambahkan")

def masuklayanan():
    nama = input("Masukkan nama player: ")

    if nama not in dataplayer:
        print("Player tidak ditemukan")
        return

    antriandungeon.append(nama)
    dataplayer[nama] = "menunggu raid"

    riwayatdungeon.append(nama + " masuk antrian")
    logaktivitas.append(nama + " masuk antrian")

    print("Masuk antrian raid")

def proseslayanan():
    if not antriandungeon:
        print("Antrian kosong")
        return

    print("\nSebelum diproses:")
    print(list(antriandungeon))

    tim = []

    for i in range(3):
        if antriandungeon:
            tim.append(antriandungeon.popleft())

    for p in tim:
        dataplayer[p] = "selesai raid"

    hasil = ", ".join(tim)
    riwayatdungeon.append(hasil + " raid selesai")
    logaktivitas.append(hasil + " raid selesai")

    print("\nRaid berjalan:", hasil)

    print("\nSesudah diproses:")
    print(list(antriandungeon))

def lihatdata():
    print("\nData player:")
    for nama, status in dataplayer.items():
        print(nama, "-", status)

def lihatantrian():
    print("Antrian raid:", list(antriandungeon))

def lihatriwayat():
    print("Riwayat aktivitas:")
    for i in riwayatdungeon[::-1]:
        print(i)

def caridata():
    nama = input("Masukkan nama yang dicari: ")

    if nama in dataplayer:
        print("Data:", nama, "-", dataplayer[nama])
    else:
        print("Data tidak ditemukan")

while True:
    tampiljudul()

    print("\n" + "=" * 10 + " RAID DUNGEON SYSTEM " + "=" * 10)
    print("1. Tambah Data Player")
    print("2. Masuk Antrian Raid")
    print("3. Proses Raid")
    print("4. Lihat Data Player")
    print("5. Lihat Antrian")
    print("6. Lihat Riwayat")
    print("7. Cari Data")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambahdata()
    elif pilih == "2":
        masuklayanan()
    elif pilih == "3":
        proseslayanan()
    elif pilih == "4":
        lihatdata()
    elif pilih == "5":
        lihatantrian()
    elif pilih == "6":  
        lihatriwayat()
    elif pilih == "7":
        caridata()
    elif pilih == "0":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")