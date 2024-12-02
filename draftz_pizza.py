import csv
import os
from datetime import datetime

# Fungsi autentikasi
def check_user_exists(username):
    if not os.path.exists('users.csv'):
        return False
    
    with open('users.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        return any(row['username'] == username for row in csv_reader)

def register_user():
    print("\n=== SIGN UP PENGGUNA BARU POKER PIZZA ===")
    
    while True:
        username = input("Username: ")
        if check_user_exists(username):
            print("Username sudah digunakan. Silakan pilih username lain.")
            continue
            
        if not username.strip():
            print("Username tidak boleh kosong.")
            continue
            
        break
    
    while True:
        password = input("Password: ")
        if len(password) < 6:
            print("Password harus minimal 6 karakter.")
            continue
        
        confirm_password = input("Konfirmasi Password: ")
        if password != confirm_password:
            print("Password tidak cocok. Silakan coba lagi.")
            continue
            
        break
    
    # Membuat file CSV jika belum ada
    if not os.path.exists('users.csv'):
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'nama_lengkap', 'no_telepon', 'alamat', 'tanggal_daftar'])
    
    # Membuat data pengguna
    tanggal_daftar = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Menyimpan data pengguna
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, '', '', '', tanggal_daftar])
    
    print("\nSign up berhasil!")
    
    # Return user data untuk auto-login
    return {
        'username': username,
        'password': password,
        'nama_lengkap': '',
        'no_telepon': '',
        'alamat': '',
        'tanggal_daftar': tanggal_daftar
    }

def login():
    print("\n=== LOGIN POKER PIZZA ===")
    
    if not os.path.exists('users.csv'):
        print("Belum ada pengguna terdaftar. Silakan sign up terlebih dahulu.")
        return None
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")
        
        with open('users.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['username'] == username and row['password'] == password:
                    print(f"\nLogin Berhasil!")
                    print(f"\nSelamat datang di Poker Pizza, {username}!")
                    return row
        
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Username atau password salah. Sisa percobaan: {remaining_attempts}")
    
    print("Terlalu banyak percobaan gagal. Silakan coba lagi nanti.")
    return None

# Fungsi pemesanan pizza
def hitung_biaya_keju(jenis_keju):
    harga_keju = {
        "cheddar": 10000,
        "mozzarella": 12000,
        "parmesan": 15000
    }
    return harga_keju.get(jenis_keju, 0)

def hitung_biaya_topping(nama_topping):
    harga_topping = {
        # Topping Rp 10.000
        "bawang": 10000,
        "jagung": 10000,
        "olive": 10000,
        "nanas": 10000,
        
        # Topping Rp 12.000
        "jamur": 12000,
        "paprika": 12000,
        "sosis ayam": 12000,
        "parsley": 12000,
        "tuna": 12000,
        "jalapeno": 12000,
        
        # Topping Rp 15.000
        "pepperoni": 15000,
        "sosis sapi": 15000,
        "meatball": 15000,
        "beef burger": 15000,
        "macaroni": 15000
    }
    return harga_topping.get(nama_topping.lower(), 0)

def simpan_pesanan(pesanan, user_data):
    # Membuat file riwayat pesanan jika belum ada
    if not os.path.exists('order_history.csv'):
        with open('order_history.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'tanggal', 'ukuran', 'saus', 'keju', 'topping', 'total_biaya', 'status_pengiriman', 'nama_penerima', 'no_telepon', 'alamat'])
    
    # Waktu pemesanan
    tanggal = pesanan.get('waktu_pemesanan', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    topping_str = ','.join(pesanan['topping'])
    
    # Menyimpan pesanan ke file
    with open('order_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            user_data['username'],
            tanggal,
            pesanan['ukuran'],
            pesanan['saus'],
            pesanan['keju'],
            topping_str,
            pesanan['total_biaya'],
            'Diproses',
            pesanan.get('nama_penerima', ''),
            pesanan.get('no_telepon', ''),
            pesanan.get('alamat', '')
        ])

def lihat_riwayat_pesanan(username):
    if not os.path.exists('order_history.csv'):
        print("\nBelum ada riwayat pesanan.")
        return
    
    print("\n=== RIWAYAT PESANAN POKER PIZZA ===")
    found = False
    
    with open('order_history.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['username'] == username:
                found = True
                print("\nTanggal:", row['tanggal'])
                print(f"Ukuran Pizza      : {row['ukuran'].capitalize()}")
                print(f"Saus              : {row['saus'].capitalize()}")
                print(f"Keju              : {row['keju'].capitalize()}")
                print(f"Topping           : {row['topping']}")
                print(f"Total             : Rp {int(float(row['total_biaya'])):,}")
                print(f"Status            : {row['status_pengiriman']}")
                if row['nama_penerima']:
                    print(f"Nama Penerima     : {row['nama_penerima']}")
                    print(f"Nomor Telepon     : {row['no_telepon']}")
                    print(f"Alamat            : {row['alamat']}")
                print("-" * 50)
    
    if not found:
        print("\nAnda belum memiliki riwayat pesanan.")

def menu_utama(user_data):
    semua_pesanan = []

    while True:
        print("\nMenu Utama Poker Pizza:")
        print("1. Pesan Pizza")
        print("2. Lihat Pesanan")
        print("3. Cancel Pesanan")
        print("4. Checkout")
        print("5. Lihat Riwayat Pesanan")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            pesanan_baru = {}
            
            # Ukuran Pizza
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
                    break
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            
            # Saus
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
                    break
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            
            # Keju
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
                    break
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            
            # Topping
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
            biaya_saus = 10000
            biaya_keju = hitung_biaya_keju(keju)
            
            if dasar == "kecil":
                biaya_dasar = 25000
            elif dasar == "sedang":
                biaya_dasar = 35000
            else:
                biaya_dasar = 45000
            
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
            print("\nPesanan berhasil ditambahkan!")
            
        elif pilihan == "2":
            if not semua_pesanan:
                print("\nTidak ada pesanan saat ini.")
                continue
            
            print("\n=== DAFTAR PESANAN ===")
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
                    print(f"- {t.capitalize():15} : Rp {hitung_biaya_topping(t):,}")
                print(f"Total Biaya Topping   : Rp {pesanan['biaya_topping']:,}")
                print(f"Total Pizza #{idx}    : Rp {pesanan['total_biaya']:,}")
                print("-" * 50)
            
        elif pilihan == "3":
            if not semua_pesanan:
                print("\nTidak ada pesanan untuk dibatalkan.")
                continue
            
            while True:
                print("\n=== BATALKAN PESANAN ===")
                print("0. Kembali ke Menu Utama")
                for idx, pesanan in enumerate(semua_pesanan, 1):
                    print(f"{idx}. Pizza {pesanan['ukuran'].capitalize()} - Rp {pesanan['total_biaya']:,}")
                
                try:
                    pilih_batal = input("\nMasukkan nomor pizza yang ingin dibatalkan (0 untuk kembali): ")
                    
                    if pilih_batal == '0':
                        print("\nKembali ke menu utama...")
                        break
                        
                    pilih_batal = int(pilih_batal)
                    if 1 <= pilih_batal <= len(semua_pesanan):
                        batalkan = semua_pesanan.pop(pilih_batal - 1)
                        print(f"\nPesanan pizza {batalkan['ukuran'].capitalize()} berhasil dibatalkan.")
                        break
                    else:
                        print("Nomor pizza tidak valid.")
                except ValueError:
                    print("Masukkan nomor yang valid.")
                    
        elif pilihan == "4":
            if not semua_pesanan:
                print("\nTidak ada pesanan untuk dicheckout.")
                continue
                
            print("\nApakah Anda ingin ambil sendiri atau diantar?")
            print("Jika Anda ambil sendiri, Anda mendapat diskon 20%")
            pesanan_pizza = input("Ketik 'ambil' atau 'antar': ").lower()
            
            # Data delivery
            nama_penerima = ""
            no_telepon = ""
            alamat = ""
            
            # Hitung total 
            total_keseluruhan = sum(pesanan['total_biaya'] for pesanan in semua_pesanan)
            
            if pesanan_pizza == "ambil":
                pengurangan_biaya = total_keseluruhan * (20 / 100)
                total_keseluruhan = total_keseluruhan - pengurangan_biaya
                diskon = True
            else:
                diskon = False
                pengurangan_biaya = 0
                print("\nMasukkan data pengiriman:")
                nama_penerima = input("Nama penerima       : ")
                while True:
                    no_telepon = input("Nomor telepon       : ")
                    if no_telepon.isdigit() and len(no_telepon) >= 12:
                        break
                    print("Nomor telepon tidak valid. Masukkan minimal 12 digit angka.")
                alamat = input("Alamat lengkap      : ")
                
                # Tambahkan data pengiriman ke setiap pesanan
                for pesanan in semua_pesanan:
                    pesanan['nama_penerima'] = nama_penerima
                    pesanan['no_telepon'] = no_telepon
                    pesanan['alamat'] = alamat           