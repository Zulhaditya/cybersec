import zipfile

def brute_force_zip(zip_file, wordlist):
    with zipfile.ZipFile(zip_file, 'r') as zf:
        with open(wordlist, 'r') as wf:
            for line in wf:
                password = line.strip()
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"[SUKSES!] Password ditemukan: {password}")
                    return password
                except (RuntimeError, zipfile.BadZipFile):
                    pass
            print("[GAGAL! Password tidak ada didalam wordlist.")
            return None

if __name__ == "__main__":
    zip_path = input("Enter the path to the ZIP file: ")
    wordlist_path = input("Enter the path to the wordlist file: ")
    brute_force_zip(zip_path, wordlist_path)

