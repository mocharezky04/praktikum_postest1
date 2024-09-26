# program menghitung gaji karyawan berdasarkan jam kerja dan tarif kerja.

# Login User, NIM, dan Prodi
print("Tolong Login Menggunakan Nama, NIM, dan Prodi\n")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
prodi = input("Masukkan Prodi: ")

# kode Selamat datang untuk user
print("\nSelamat datang", nama, "dengan NIM", nim, "dari Prodi", prodi)

while True: # Menggunakan while untuk mengulang pertanyaan atau menghitung gaji lagi
    # Menggunakan input untuk jam kerja dan tarif kerja dan menghitung total gaji
    jam_kerja = int(input("\nMasukkan berapa jam kamu bekerja: "))
    tarif_kerja = int(input("Masukkan tarif kerja per jam: Rp."))
    total_gaji = jam_kerja * tarif_kerja

    # Membuat percabangan untuk menentukan apakah jam kerja karyawan lebih dari 160 jam.
    # Jika lebih, tambahkan bonus sebesar 10% dari total gaji.
    # Sedangkan jika tidak mencapai lebih dari 160 jam, maka tidak mendapatkan bonus
    if int(jam_kerja) > 160:
        gaji_bonus = 0.10 * total_gaji # menghitung tambahan gaji bonus
        total_gaji += gaji_bonus
        print("\nSelamat anda mendapatkan bonus sebesar 10% dari total gaji")
        print("dan ini gaji anda setelah mendapatkan bonus:", total_gaji)
    else:
        print("\nMaaf anda tidak mendapatkan bonus karena tidak melebihi 160 jam kerja")
        print("Dan ini gaji anda sekarang:", total_gaji)

    # Menerapkan perulangan untuk memberikan pilihan apakah ingin menghitung gaji lagi atau keluar dari program
    print('\nSilahkan pilih pilihan berikut:\n 1.ingin menghitung gaji lagi?\n 2.keluar dari program\n')
    pilihan = int(input('Masukan pilihan anda(nomor 1 atau 2): '))
    if pilihan == 1:
        continue # Menghitung gaji lagi
    elif pilihan == 2:
        print("\nTerima Kasih telah menggunakan program python ini. anda akan dikeluarkan dari program ini dan selamat tinggal!")
        break # keluar dari program karena memilih untuk keluar atau no.2
    else:
        print("\nMaaf, Pilihan tidak ada. Anda akan secara otomatis dikeluarkan dalam program ini")
        break # Keluar dari program dikarenakan tidak ada pilihan selain 1 dan 2
