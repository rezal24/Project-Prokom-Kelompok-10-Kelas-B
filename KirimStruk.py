import os
import smtplib
import pywhatkit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import time
import pyautogui
import keyboard
import webbrowser
from urllib.parse import quote

def kirim_struk_email(file_struk, nama_penerima):
    """
    Mengirim struk pembelian melalui email menggunakan SMTP
    """
    # Validasi file exists
    if not os.path.isfile(file_struk):
        return False, f"File struk tidak ditemukan: {file_struk}"
        
    # Konfigurasi email
    EMAIL_PENGIRIM = "pokerpizza10@gmail.com"
    PASSWORD_EMAIL = "arso mxtr kpea quzc"  # Ganti dengan App Password
    EMAIL_PENERIMA = "raulmabbasy@gmail.com"
    
    # Buat objek MIME
    pesan = MIMEMultipart()
    pesan['From'] = EMAIL_PENGIRIM
    pesan['To'] = EMAIL_PENERIMA
    pesan['Subject'] = f'Struk Pembelian Poker Pizza - {datetime.now().strftime("%Y-%m-%d %H:%M")}'
    
    # Tambahkan body email
    body = f"""Halo {nama_penerima},

Berikut adalah struk pembelian Anda dari Poker Pizza.

Terima kasih telah berbelanja di Poker Pizza!

Salam,
Tim Poker Pizza"""
    
    pesan.attach(MIMEText(body, 'plain'))
    
    # Lampirkan file struk
    with open(file_struk, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_struk))
        pesan.attach(attachment)
    
    try:
        # Buat koneksi SMTP dengan Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_PENGIRIM, PASSWORD_EMAIL)
            server.send_message(pesan)
        return True, "Struk berhasil dikirim melalui email!"
    except Exception as e:
        return False, f"Gagal mengirim email: {str(e)}"

def kirim_struk_whatsapp(file_struk):
    """
    Mengirim struk pembelian melalui WhatsApp secara otomatis
    """
    try:
        # Baca isi file struk
        with open(file_struk, 'r', encoding='utf-8') as f:
            isi_struk = f.read()
        
        # Nomor WhatsApp penerima dan pengirim
        NOMOR_WHATSAPP = "6285771108999"
        
        # Format pesan
        pesan = f"""*STRUK PEMBELIAN POKER PIZZA*

{isi_struk}"""
        
        # Encode pesan untuk URL
        encoded_pesan = quote(pesan)
        
        # Buat URL WhatsApp
        url = f"https://web.whatsapp.com/send?phone={NOMOR_WHATSAPP}&text={encoded_pesan}"
        
        # Buka browser dengan URL WhatsApp
        webbrowser.open(url)
        
        # Tunggu hingga WhatsApp Web terbuka dan memuat
        time.sleep(15)  # Sesuaikan waktu tunggu dengan kecepatan internet
        
        # Tekan Enter untuk mengirim
        pyautogui.press('enter')
        
        # Tunggu sebentar untuk memastikan pesan terkirim
        time.sleep(3)
        
        # Tutup tab browser
        pyautogui.hotkey('ctrl', 'w')
        
        return True, "Struk berhasil dikirim melalui WhatsApp!"
    except Exception as e:
        return False, f"Gagal mengirim WhatsApp: {str(e)}"

def kirim_struk_otomatis(file_struk, nama_penerima):
    """
    Mengirim struk melalui email dan WhatsApp secara otomatis
    """
    print("\nMengirim struk pembelian...")
    
    # Kirim melalui email
    success_email, message_email = kirim_struk_email(file_struk, nama_penerima)
    print(message_email)
    
    # Tunggu sebentar sebelum mengirim WhatsApp
    time.sleep(2)
    
    # Kirim melalui WhatsApp
    success_wa, message_wa = kirim_struk_whatsapp(file_struk)
    print(message_wa)
    
    return success_email and success_wa