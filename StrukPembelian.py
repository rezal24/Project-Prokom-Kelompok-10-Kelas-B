import os
import traceback
import time
from datetime import datetime

def simpan_struk_pembelian(pesanan, total_keseluruhan, diskon, pengurangan_biaya, user_data, pesanan_pizza):
    try:
        # Buat direktori untuk struk jika belum ada
        os.makedirs('struk', exist_ok=True)
        
        # Gunakan timestamp sebagai nama file untuk menghindari konflik
        waktu_pemesanan = datetime.now()
        nama_file = f"struk/struk_{user_data['username']}_{waktu_pemesanan.strftime('%Y%m%d_%H%M%S')}.txt"
        
        while True:
            # Tambahkan print untuk path file
            print(f"Cek struk-mu di: \n{os.path.abspath(nama_file)}")
            
            with open(nama_file, 'w', encoding='utf-8') as file:
                # Header Struk
                file.write("=" * 50 + "\n")
                file.write("           STRUK PEMBELIAN POKER PIZZA\n")
                file.write("=" * 50 + "\n")
                file.write(f"Tanggal: {waktu_pemesanan.strftime('%d %B %Y')}\n")
                file.write(f"Waktu  : {waktu_pemesanan.strftime('%H:%M:%S')}\n")
                file.write(f"Kasir  : {user_data['username']}\n")
                file.write("=" * 50 + "\n")
                
                # Detail Setiap Pizza
                for idx, pizza in enumerate(pesanan, 1):
                    file.write(f"\nPizza #{idx}\n")
                    file.write(f"Ukuran Pizza          : {pizza['ukuran'].capitalize()}\n")
                    file.write(f"Biaya Dasar           : Rp {pizza['biaya_dasar']:,}\n")
                    file.write(f"Saus                  : {pizza['saus'].capitalize()}\n")
                    file.write(f"Biaya Saus            : Rp {pizza['biaya_saus']:,}\n")
                    file.write(f"Keju                  : {pizza['keju'].capitalize()}\n")
                    file.write(f"Biaya Keju            : Rp {pizza['biaya_keju']:,}\n")
                    
                    file.write("\nTopping:\n")
                    for t in pizza['topping']:
                        file.write(f"- {t.capitalize():15}     : Rp 10000\n")  # Hardcoded for debugging
                    
                    file.write(f"Total Biaya Topping   : Rp {pizza['biaya_topping']:,}\n")
                    file.write(f"Subtotal Pizza #{idx}     : Rp {pizza['total_biaya']:,}\n")
                    file.write("-" * 50 + "\n")
                
                # Informasi Pengiriman (jika diantar)
                if pesanan_pizza == "antar":
                    file.write("\nInformasi Pengiriman:\n")
                    file.write(f"Nama Penerima         : {pesanan[0].get('nama_penerima', 'N/A')}\n")
                    file.write(f"Nomor Telepon         : {pesanan[0].get('no_telepon', 'N/A')}\n")
                    file.write(f"Alamat                : {pesanan[0].get('alamat', 'N/A')}\n")
                    file.write(f"Biaya Pengiriman      : Gratis\n")
                
                # Ringkasan Biaya
                file.write("\nRingkasan Biaya:\n")
                file.write(f"Total Pesanan         : Rp {total_keseluruhan:,}\n")
                
                if diskon:
                    file.write(f"Diskon (20%)          : Rp {round(pengurangan_biaya):,}\n")
                else:
                    file.write("Diskon                : Rp 0\n")
                
                file.write(f"Total Akhir           : Rp {round(total_keseluruhan):,}\n")
                file.write("=" * 50 + "\n")
                file.write("Terima kasih telah berbelanja di Poker Pizza!\n")
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
    
    except Exception as e:
        print("\n--- Error saat menyimpan struk ---")
        print(f"Error: {e}")
        traceback.print_exc()