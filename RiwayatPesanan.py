import os
import csv
from datetime import datetime

def simpan_pesanan(pesanan, user_data):
    # Membuat file riwayat pesanan jika belum ada
    if not os.path.exists('order_history.csv'):
        with open('order_history.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'tanggal', 'ukuran', 'saus', 'keju', 'topping', 'total_biaya', 'nama_penerima', 'no_telepon', 'alamat'])
    
    # Gunakan waktu_pemesanan dari pesanan jika tersedia, jika tidak gunakan waktu saat ini
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
            pesanan.get('nama_penerima', ''),
            pesanan.get('no_telepon', ''),
            pesanan.get('alamat', '')
        ])

def lihat_riwayat_pesanan(username):
    if not os.path.exists('order_history.csv'):
        print("Belum ada riwayat pesanan.")
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
                if row['nama_penerima']:
                    print(f"Nama Penerima     : {row['nama_penerima']}")
                    print(f"Nomor Telepon     : {row['no_telepon']}")
                    print(f"Alamat            : {row['alamat']}")
                print("-" * 50)
    
    if not found:
        print("\nAnda belum memiliki riwayat pesanan.")