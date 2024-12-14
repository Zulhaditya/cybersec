import os

# nama file untuk menyimpan data
FILENAME = "glossary.txt"

def display_menu():
    print("\nCatatan SKB Sandiman Ahli Pertama")
    print("1. Tambah istilah")
    print("2. Lihat semua istilah")
    print("3. Cari istilah")
    print("4. Edit istilah")
    print("5. Hapus istilah")
    print("6. Keluar")

def load_glossary():
    # menampilkan catatan dari file
    glossary = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                term, description = line.strip().split(":", 1)
                glossary[term] = description
            return glossary

def save_glossary(glossary):
    # menyimpan catatan ke file
    with open(FILENAME, "w") as file:
        for term, description in glossary.items():
            file.write(f"{term}:{description}\n")

def add_term(glossary):
    term = input("Masukkan istilah: ").strip()
    if term in glossary:
        print(f"Istilah '{term}' sudah ada di daftar.")
        return
    description = input("Masukkan deskripsi untuk istilah: ")
    glossary[term] = description
    save_glossary(glossary)
    print(f"Istilah '{term}' berhasil ditambahkan.")

def edit_description(glossary):
    term = input("Masukkan istilah yang akan diedit: ").strip()
    if term in glossary:
        print(f"Deskripsi saat ini '{term}': {glossary[term]}")
        new_description = input("Masukkan deskripsi baru: ").strip()
        glossary[term] = new_description
        save_glossary(glossary)
        print(f"Deskripsi untuk '{term}' berhasil diperbaharui.")
    else:
        print(f"Istilah '{term}' tidak ditemukan.")

def view_terms(glossary):
    if not glossary:
        print("Belum ada istilah dalam daftar.")
        return
    print("\nDaftar Istilah:")
    for term, description in glossary.items():
        print(f"- {term}: {description}")

def search_term(glossary):
    search = input("Masukkan istilah yang ingin dicari: ").strip()
    if search in glossary:
        print(f"{search}: {glossary[search]}")
    else:
        print(f"Istilah '{search}' tidak ditemukan.")

def delete_term(glossary):
    term = input("Masukkan istilah yang ingin dihapus: ").strip()
    if term in glossary:
        del glossary[term]
        save_glossary(glossary)
        print(f"Istilah '{term}' berhasil dihapus.")
    else:
        print(f"Istilah '{term} tidak ditemukan dalam daftar.'")

def main():
    glossary = load_glossary()
    while True:
        display_menu()
        choice = input("Pilih opsi (1-4): ").strip()
        if choice == "1":
            add_term(glossary)
        elif choice == "2":
            view_terms(glossary)
        elif choice == "3":
            search_term(glossary)
        elif choice == "4":
            edit_description(glossary)
        elif choice == "5":
            delete_term(glossary)
        elif choice == "6":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

