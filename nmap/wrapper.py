import nmap
import socket

class NmapWrapper:
    def __init__(self, target_network):
        # Target network bisa berupa '192.168.1.0/24'
        self.target_network = target_network
        self.nm = nmap.PortScanner()

    def scan(self):
        print(f"Scanning network: {self.target_network}")
        # Menjalankan Nmap untuk memindai semua IP di jaringan lokal
        self.nm.scan(hosts=self.target_network, arguments='-sn')  # -sn untuk ping scan
        self._parse_results()

    def _parse_results(self):
        # Parsing hasil scan
        print("Device yang terhubung ke jaringan lokal:")
        for index, host in enumerate(self.nm.all_hosts(), start=1): # Menambahkan nomor urut
            if self.nm[host].state() == "up":
                print(f"{index}. Host {host} terhubung!")
            else:
                print(f"Host {host} tidak terhubung.")

    def get_local_ip_range(self):
        # Mengambil IP lokal dan menghasilkan subnet untuk scan
        local_ip = socket.gethostbyname(socket.gethostname())
        subnet = '.'.join(local_ip.split('.')[:-1]) + '.0/24'
        return subnet

if __name__ == "__main__":
    nmap_wrapper = NmapWrapper(target_network="192.168.1.0/24")
    nmap_wrapper.scan()
