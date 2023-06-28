import socket
import os

def send_file(filename, host, port):
    # ایجاد یک اتصال سوکت
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # اتصال به سرور مقصد
        client_socket.connect((host, port))
        
        # باز کردن فایل برای خواندن
        with open(filename, 'rb') as file:
            # ارسال طول نام فایل به عنوان هدر
            filename_length = len(filename)
            client_socket.sendall(filename_length.to_bytes(4, byteorder='big'))
            
            # ارسال نام فایل
            client_socket.sendall(filename.encode())
            
            # خواندن داده‌های فایل به صورت بخش‌هایی و ارسال آنها
            while True:
                data = file.read(1048576)  # خواندن یک بخش از فایل (مثلاً 1048576 بایت معادل 1 مگابایت)
                if not data:
                    break  # اگر دیگر داده‌ای برای خواندن نباشد، حلقه را متوقف کنید
                client_socket.sendall(data)  # ارسال بخش خوانده شده
                
    except Exception as e:
        print(f"خطا در ارسال فایل: {str(e)}")
        
    finally:
        # بستن اتصال سوکت
        client_socket.close()

# استفاده از تابع برای ارسال فایل
send_file('FileName.exe', 'localhost', 8888)