import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} terbuka!")
                    open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}!")
    return open_ports

if __name__ == "__main__":
    target_host = input("Masukkan target host (contoh: 127.0.0.1): ")
    target_ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443]
    open_ports = scan_ports(target_host, target_ports)
    print(f"Port terbuka di {target_host}: {open_ports}")

"""
Berikut adalah 10 port umum yang sering digunakan beserta layanan terkait:

Port 20 - FTP Data
Digunakan untuk transfer data dalam protokol FTP (File Transfer Protocol).

Port 21 - FTP Control
Digunakan untuk koneksi kontrol pada protokol FTP.

Port 22 - SSH (Secure Shell)
Digunakan untuk koneksi remote yang aman ke server.

Port 23 - Telnet
Digunakan untuk koneksi remote yang tidak aman (umumnya sudah jarang digunakan).

Port 25 - SMTP (Simple Mail Transfer Protocol)
Digunakan untuk mengirim email.

Port 53 - DNS (Domain Name System)
Digunakan untuk layanan pencarian domain ke alamat IP.

Port 80 - HTTP (Hypertext Transfer Protocol)
Digunakan untuk mengakses halaman web (tanpa enkripsi).

Port 110 - POP3 (Post Office Protocol v3)
Digunakan untuk mengambil email dari server.

Port 143 - IMAP (Internet Message Access Protocol)
Digunakan untuk mengakses email di server.

Port 443 - HTTPS (HTTP Secure)
Digunakan untuk mengakses halaman web dengan koneksi terenkripsi.    

"""
