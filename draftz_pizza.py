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