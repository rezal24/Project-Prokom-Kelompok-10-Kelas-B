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
        print ("!!!! Password Minimal 6 Karakter !!!!")
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
    
    os.system("cls")
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