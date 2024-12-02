import csv
import os


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
