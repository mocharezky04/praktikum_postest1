# program menghitung gaji karyawan berdasarkan jam kerja dan tarif kerja.

# Login Sederhana User, NIM, dan Prodi
print("Tolong Login Menggunakan Nama, NIM, dan Prodi\n")
nama = input("Masukkan Nama: ") # Input Nama

# Input Prodi
prodi = input("Masukkan Prodi: ") 

# Proses input NIM dengan menggunakan while untuk terus meminta input NIM hingga pengguna memasukkan NIM yang benar (berupa angka).
while True: 
    nim = input("Masukkan NIM: ")
    if nim.isdigit(): # Mengecek apakah NIM hanya berisi angka
        break # Jika benar, loop akan berhenti dengan break
    else: # Jika salah(ada huruf atau selain angka), program akan meminta user untuk input nim ulang dan akan diberi peringatan
        print("Tolong isi dengan angka dan bukan huruf ya!")

# menampilkan Selamat datang atau sapaan untuk user
print("\nSelamat datang", nama, "dari Prodi", prodi, "dengan NIM", nim,)

while True: # Menggunakan while untuk mengulang pertanyaan atau menghitung gaji lagi
    # Menggunakan input untuk jam kerja dan tarif kerja serta menghitung total gaji
    jam_kerja = int(input("\nMasukkan berapa jam kamu bekerja: "))
    tarif_kerja = int(input("Masukkan tarif kerja per jam: Rp."))
    total_gaji = jam_kerja * tarif_kerja # rumus atau perhitungan untuk mencari total gaji

    # Membuat percabangan untuk menentukan apakah jam kerja karyawan lebih dari 160 jam.
    # Jika lebih, tambahkan bonus sebesar 10% dari total gaji.
    # Sedangkan jika tidak mencapai lebih dari 160 jam, maka tidak mendapatkan bonus
    if int(jam_kerja) > 160:
        gaji_bonus = 0.10 * total_gaji # menghitung tambahan gaji bonus
        total_gaji += gaji_bonus # total gaji ditambah gaji bonus yyang telah dihitung
        print("\nSelamat anda mendapatkan bonus sebesar 10% dari total gaji")
        print("dan ini gaji anda setelah mendapatkan bonus:", total_gaji) # menampilkan total gaji yang sudah ditambah dengan gaji bonus
    else:
        print("\nMaaf anda tidak mendapatkan bonus karena tidak melebihi 160 jam kerja")
        print("Dan ini gaji anda sekarang:", total_gaji) # menampilkan gaji yang tidak dihitung dengan gaji bonus

    # Menerapkan perulangan untuk memberikan pilihan apakah ingin menghitung gaji lagi atau keluar dari program
    print('\nSilahkan pilih pilihan berikut:\n 1.ingin menghitung gaji lagi?\n 2.keluar dari program\n') # pilihan untuk user apakah user mau menghitung gaji lagi atau tidak
    pilihan = int(input('Masukan pilihan anda(nomor 1 atau 2): ')) 
    if pilihan == 1: 
        continue # User akan menghitung gaji lagi jika memilih no.1
    elif pilihan == 2:
        print("\nTerima Kasih telah menggunakan program python ini. anda akan dikeluarkan dari program ini dan selamat tinggal!")
        break # user akan keluar dari program jika memilih untuk keluar atau no.2
    else:
        print("\nMaaf, Pilihan tidak ada. Anda akan secara otomatis dikeluarkan dalam program ini")
        break # user akan Keluar dari program atau otomatis akan keluar dari program jika memilih selain nomor 1 dan 2
