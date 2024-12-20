import csv
import os
import time
from datetime import datetime
from RegisterUser import check_user_exists, register_user
from Login import login
from RiwayatPesanan import lihat_riwayat_pesanan, simpan_pesanan
from StrukPembelian import simpan_struk_pembelian
from HitungBiaya import hitung_biaya_dasar, hitung_biaya_keju, hitung_biaya_saus, hitung_biaya_topping
from KirimStruk import kirim_struk_email, kirim_struk_otomatis, kirim_struk_whatsapp
def menu_utama(user_data):
    semua_pesanan = []
    
    while True:
        print("\nMenu Utama Poker Pizza:")
        print("1. Pesan Pizza")
        print("2. Lihat Pesanan")
        print("3. Cancel Pesanan")
        print("4. Checkout")
        print("5. Lihat Riwayat Pesanan")
        print("6. Logout")
        
        pilihan = input("Pilih menu (1-6): ")
        os.system("cls")
        
        if pilihan == "1":
            pesanan_baru = {}
            
            print("\n=== PILIHAN UKURAN PIZZA ===")
            print("1) Kecil           Rp 25.000")
            print("2) Sedang          Rp 35.000") 
            print("3) Besar           Rp 45.000")
            
            dasar_opsi = {
                '1': 'kecil',
                '2': 'sedang', 
                '3': 'besar'
            }
            
            while True:
                dasar_input = input("\nPilih ukuran pizza (1/2/3): ")
                if dasar_input in dasar_opsi:
                    dasar = dasar_opsi[dasar_input]
                    os.system("cls")
                    break
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
                
            print("\n=== PILIHAN SAUS (Rp 10.000) ===")
            print("1) Saus Tomat")
            print("2) Saus Pesto")
            print("3) Saus BBQ")
            
            saus_opsi = {
                '1': 'tomat',
                '2': 'pesto',
                '3': 'bbq'
            }
            
            while True:
                saus_input = input("\nPilih saus (1/2/3): ")
                if saus_input in saus_opsi:
                    saus = saus_opsi[saus_input]
                    os.system("cls")
                    break
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
                
            print("\n=== PILIHAN KEJU ===")
            print("1) Keju Cheddar    Rp 10.000")
            print("2) Keju Mozzarella Rp 12.000")
            print("3) Keju Parmesan   Rp 15.000")
            
            keju_opsi = {
                '1': 'cheddar',
                '2': 'mozzarella',
                '3': 'parmesan'
            }
            
            while True:
                keju_input = input("\nPilih keju (1/2/3): ")
                if keju_input in keju_opsi:
                    keju = keju_opsi[keju_input]
                    os.system("cls")
                    break
                    
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
                
            print("\n=== PILIHAN TOPPING ===")
            print("1) Bawang          Rp 10.000")
            print("2) Jagung          Rp 10.000")
            print("3) Olive           Rp 10.000")
            print("4) Nanas           Rp 10.000")
            print("5) Jamur           Rp 12.000")
            print("6) Paprika         Rp 12.000")
            print("7) Sosis Ayam      Rp 12.000")
            print("8) Parsley         Rp 12.000")
            print("9) Tuna            Rp 12.000")
            print("10) Jalapeno       Rp 12.000")
            print("11) Pepperoni      Rp 15.000")
            print("12) Sosis Sapi     Rp 15.000")
            print("13) Meatball       Rp 15.000")
            print("14) Beef Burger    Rp 15.000")
            print("15) Macaroni       Rp 15.000")
            print("\n0) Selesai memilih topping")
            
            topping_opsi = {
                '1': 'bawang', '2': 'jagung', '3': 'olive', '4': 'nanas', 
                '5': 'jamur', '6': 'paprika', '7': 'sosis ayam', 
                '8': 'parsley', '9': 'tuna', '10': 'jalapeno', 
                '11': 'pepperoni', '12': 'sosis sapi', '13': 'meatball', 
                '14': 'beef burger', '15': 'macaroni'
            }
            
            topping = []
            biaya_topping = 0
            
            while True:
                topping_input = input("\nPilih topping (0-15, 0 untuk selesai): ")
                if topping_input == '0':
                    break
                
                if topping_input not in topping_opsi:
                    print("Pilihan tidak valid. Silakan pilih 1-15 atau 0.")
                    continue
                
                tambahan = topping_opsi[topping_input]
                if tambahan in topping:
                    print("Topping sudah dipilih sebelumnya.")
                    continue
                
                topping.append(tambahan)
                biaya_topping += hitung_biaya_topping(tambahan)
                print(f"Topping {tambahan.capitalize()} ditambahkan.")
                
            # Hitung biaya
            biaya_dasar = hitung_biaya_dasar(dasar)
            biaya_saus = hitung_biaya_saus(saus)
            biaya_keju = hitung_biaya_keju(keju)
            
            total_biaya = biaya_dasar + biaya_topping + biaya_saus + biaya_keju
            
            pesanan_baru = {
                'ukuran': dasar,
                'saus': saus,
                'keju': keju,
                'topping': topping,
                'biaya_dasar': biaya_dasar,
                'biaya_saus': biaya_saus,
                'biaya_keju': biaya_keju,
                'biaya_topping': biaya_topping,
                'total_biaya': total_biaya
            }
            
            semua_pesanan.append(pesanan_baru)
            os.system("cls")
            print("\nPesanan berhasil ditambahkan!")
            print("\nKembali ke Menu Utama...")
            time.sleep(2)
            os.system("cls")
            
        elif pilihan == "2":
            if not semua_pesanan:
                os.system("cls")
                print("Tidak ada pesanan saat ini.")
                print("\nKembali ke Menu Utama...")
                time.sleep(2)
                os.system("cls")
                continue
            
            while True:    
                print(f"-" * 50)
                print("=== DAFTAR PESANAN ===")
                for idx, pesanan in enumerate(semua_pesanan, 1):
                    print(f"\nPizza #{idx}")
                    print(f"Ukuran Pizza          : {pesanan['ukuran'].capitalize()}")
                    print(f"Biaya Dasar           : Rp {pesanan['biaya_dasar']:,}")
                    print(f"Saus                  : {pesanan['saus'].capitalize()}")
                    print(f"Biaya Saus            : Rp {pesanan['biaya_saus']:,}")
                    print(f"Keju                  : {pesanan['keju'].capitalize()}")
                    print(f"Biaya Keju            : Rp {pesanan['biaya_keju']:,}")
                    print("\nTopping:")
                    for t in pesanan['topping']:
                        print(f"- {t.capitalize():15}     : Rp {hitung_biaya_topping(t):,}")
                    print(f"Total Biaya Topping   : Rp {pesanan['biaya_topping']:,}")
                    print(f"Total Pizza #{idx}        : Rp {pesanan['total_biaya']:,}")
                    print("-" * 50)
                try:
                    pilih_kembali = input("\nMasukkan 0 untuk kembali: ")
                    if pilih_kembali == '0':
                        os.system("cls")
                        print("\nKembali ke Menu Utama...")
                        time.sleep(2)
                        os.system("cls")
                        break
                    
                    pilih_kembali = int(pilih_kembali)
                    if pilih_kembali != 0:
                        os.system("cls")
                        print(f"\nMasukkan Nomor yang Valid!")
                        
                except ValueError:
                    os.system("cls")
                    print(f"\nMasukkan Nomor yang Valid!")
                    
        elif pilihan == "3":
            if not semua_pesanan:
                print("Tidak ada pesanan untuk dibatalkan.")
                print("\nKembali ke menu utama...")
                time.sleep(2)
                os.system("cls")
                continue
            
            while True:
                print("\n=== BATALKAN PESANAN ===")
                print("0. Kembali ke Menu Utama")
                for idx, pesanan in enumerate(semua_pesanan, 1):
                    print(f"{idx}. Pizza {pesanan['ukuran'].capitalize()} - Rp {pesanan['total_biaya']:,}")
                try:
                    pilih_batal = input("\nMasukkan nomor pizza yang ingin dibatalkan: ")
                    if pilih_batal == '0':
                        os.system("cls")
                        print("\nKembali ke menu utama...") 
                        time.sleep(2) 
                        os.system("cls")
                        break
                    
                    pilih_batal = int(pilih_batal)
                    if 1 <= pilih_batal <= len(semua_pesanan):
                        batalkan = semua_pesanan.pop(pilih_batal - 1)
                        os.system("cls")
                        print(f"\nPesanan pizza {batalkan['ukuran'].capitalize()} berhasil dibatalkan.")
                        print("\nKembali ke menu utama...")
                        time.sleep(2)
                        os.system("cls")
                        break
                    
                    else:
                        os.system("cls")
                        print("Nomor pizza tidak valid.")
                        
                except ValueError:
                    os.system("cls")
                    print("Masukkan nomor yang valid.")
                    
        elif pilihan == "4":
            if not semua_pesanan:
                os.system("cls")
                print("Tidak ada pesanan untuk dicheckout.")
                print("\nKembali ke menu utama...")
                time.sleep(2)
                os.system("cls")
                continue
            
            total_keseluruhan = sum(pesanan['total_biaya'] for pesanan in semua_pesanan)
            should_continue = False
                
            while True:
                print("\n=== PILIHAN PENGAMBILAN ===")
                print("1. Ambil (Diskon 20%)")
                print("2. Antar (Gratis Ongkir)")
                print("0. Kembali ke Menu Utama")
                
                try:
                    pesanan_choice = input("\nPilih metode pengambilan: ")
                    if pesanan_choice == '0':
                        os.system("cls")
                        print("\nKembali ke menu utama...") 
                        time.sleep(2) 
                        os.system("cls")
                        should_continue = True
                        break
                        
                    elif pesanan_choice == '1':
                        pesanan_pizza = "ambil"
                        pengurangan_biaya = total_keseluruhan * (20 / 100)
                        total_akhir = total_keseluruhan - pengurangan_biaya
                        diskon = True
                        os.system("cls")
                        print("Mencetak Struk Pembelian...")
                        time.sleep(2)
                        os.system("cls")
                        break
                        
                    elif pesanan_choice == '2':
                        pesanan_pizza = "antar"
                        diskon = False
                        total_akhir = total_keseluruhan
                        pengurangan_biaya = 0
                        os.system("cls")
                        
                        print("\nMasukkan data pengiriman")
                        nama_penerima = input("Nama penerima           : ")
                        
                        while True:
                            no_telepon_input = input("Nomor telepon           : (+62)").strip()
                            if no_telepon_input.isdigit() and 11 <= len(no_telepon_input) <= 12:
                                no_telepon = f"(+62){no_telepon_input}"
                                break
                            print("Nomor telepon tidak valid. Masukkan 11-12 digit nomor telepon (tanpa +62).")
                            
                        while True:
                            print("Menulis Alamat Harus Diawali Kata 'Jalan'!")
                            alamat = input("Alamat                  : ").strip()
                            if "Jalan" in alamat:
                                break
                            else:
                                print("Nama jalan harus diisi!")
                                
                        alamat_tambahan = input("Detail alamat (opsional): ")
                        alamat = f"{alamat}, {alamat_tambahan}".strip(', ')
                        
                        for pesanan in semua_pesanan:
                            pesanan['nama_penerima'] = nama_penerima
                            pesanan['no_telepon'] = no_telepon
                            pesanan['alamat'] = alamat
                            
                        os.system("cls")
                        print("Mencetak Struk Pembelian...")
                        time.sleep(2)
                        os.system("cls")
                        break
                        
                    else:
                        os.system("cls")
                        print("\nMasukkan Nomor yang Valid.")
                        time.sleep(2)
                        os.system("cls")
                        
                except ValueError:
                    os.system("cls")
                    print("\nMasukkan Nomor yang Valid.")
                    time.sleep(2)
                    os.system("cls")
                    
            if should_continue:
                continue
                    
            # Dapatkan timestamp saat ini untuk struk
            waktu_pemesanan = datetime.now()
            
            while True:
                print("\nSTRUK PEMBELIAN POKER PIZZA")
                print("=" * 50)
                print(f"Tanggal: {waktu_pemesanan.strftime('%d %B %Y')}")
                print(f"Waktu  : {waktu_pemesanan.strftime('%H:%M:%S')}")
                print("=" * 50)
                
                for idx, pesanan in enumerate(semua_pesanan, 1):
                    print(f"\nPizza #{idx}")
                    print(f"Ukuran Pizza          : {pesanan['ukuran'].capitalize()}")
                    print(f"Biaya Dasar           : Rp {pesanan['biaya_dasar']:,}")
                    print(f"Saus                  : {pesanan['saus'].capitalize()}")
                    print(f"Biaya Saus            : Rp {pesanan['biaya_saus']:,}")
                    print(f"Keju                  : {pesanan['keju'].capitalize()}")
                    print(f"Biaya Keju            : Rp {pesanan['biaya_keju']:,}")
                    print("\nTopping:")
                    for t in pesanan['topping']:
                        print(f"- {t.capitalize():15}     : Rp {hitung_biaya_topping(t):,}")
                    print(f"Total Biaya Topping   : Rp {pesanan['biaya_topping']:,}")
                    print(f"Subtotal Pizza #{idx}     : Rp {pesanan['total_biaya']:,}")
                    print("-" * 50)
                    
                    # Tambahkan waktu_pemesanan 
                    pesanan['waktu_pemesanan'] = waktu_pemesanan.strftime("%Y-%m-%d %H:%M:%S")
                
                if pesanan_pizza == "antar":
                    print("\nInformasi Pengiriman:")
                    print(f"Nama Penerima         : {nama_penerima}")
                    print(f"Nomor Telepon         : {no_telepon}")
                    print(f"Alamat                : {alamat}")
                    print(f"Biaya Pengiriman      : Gratis")
                    print(f"-" * 50)
                        
                print("\nRingkasan Biaya:")
                print(f"Total Pesanan         : Rp {total_keseluruhan:,}")
                    
                if diskon:
                    print(f"Diskon (20%)          : Rp {round(pengurangan_biaya):,}")
                else:
                    print("Diskon                : Rp 0")
                    
                print(f"Total Akhir           : Rp {round(total_akhir):,}")
                print("=" * 50)
                    
                try:
                    pilih_kembali = input("\nMasukkan 0 untuk kembali: ")
                    if pilih_kembali == '0':
                        os.system("cls")
                        print("\nTerima kasih telah berbelanja di Poker Pizza!")
                        time.sleep(2)
                        os.system("cls")
                        break
                    
                    pilih_kembali = int(pilih_kembali)
                    if pilih_kembali != 0:
                        os.system("cls")
                        print(f"\nMasukkan Nomor yang Valid!")
                        
                except ValueError:
                    os.system("cls")
                    print(f"\nMasukkan Nomor yang Valid!")
                    
            # Simpan pesanan ke riwayat
            simpan_pesanan(pesanan, user_data)
            
            # Simpan struk pembelian
            simpan_struk_pembelian(semua_pesanan, total_keseluruhan, diskon, pengurangan_biaya, user_data, pesanan_pizza)
            # Setelah simpan_struk_pembelian
            file_struk = f"struk/struk_{user_data['username']}_{waktu_pemesanan.strftime('%Y%m%d_%H%M')}.txt"
            # Reset pesanan setelah checkout
            semua_pesanan = []
            # Setelah simpan_struk_pembelian
            file_struk = f"struk/struk_{user_data['username']}_{waktu_pemesanan.strftime('%Y%m%d_%H%M')}.txt"
            # Validasi keberadaan file sebelum dikirim
            if not os.path.isfile(file_struk):
                print(f"File struk {file_struk} tidak ditemukan!")
            else:
                # Kirim struk secara otomatis
                kirim_struk_otomatis(file_struk, user_data['username'])
            time.sleep(2)
            os.system("cls")
            
        elif pilihan == "5":
            os.system("cls")
            lihat_riwayat_pesanan(user_data['username'])
            
        elif pilihan == "6":
            os.system("cls")
            print("Terima kasih telah menggunakan layanan Poker Pizza!")
            time.sleep(2)
            os.system("cls")
            break
            
        else:
            os.system("cls")
            print("\nPilihan tidak valid. Silakan pilih 1-6.")
            time.sleep(2)
            os.system("cls")
            
def main():
    while True:
        print("\n=== SELAMAT DATANG DI POKER PIZZA ===")
        print("1. Login")
        print("2. Sign Up")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            os.system("cls")
            user_data = login()
            if user_data:
                menu_utama(user_data)
        
        elif pilihan == "2":
            os.system("cls")
            user_data = register_user()  
            if user_data: 
                print(f"\nSelamat datang di Poker Pizza, {user_data['username']}!")
                menu_utama(user_data)  
        
        elif pilihan == "3":
            os.system("cls")
            print("\nTerima kasih telah menggunakan layanan Poker Pizza!")
            print("")
            break
        
        else:
            os.system("cls")
            print("\nPilihan tidak valid. Silakan pilih 1-3.")

if __name__ == "__main__":
    main()