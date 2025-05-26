import base64

def main():
    print("\nPilih opsi:")
    print("1. Encode teks")
    print("2. Decode teks")
    print("3. Keluar")
    
    while True:
        choice = input("\nMasukkan pilihan (1/2/3): ")
        
        if choice == '1':
            text = input("Masukkan teks yang akan diencode: ")
            encoded = base64.b64encode(text.encode()).decode()
            print(f"\nHasil encode: {encoded}")
            
        elif choice == '2':
            text = input("Masukkan teks yang akan didecode: ")
            try:
                decoded = base64.b64decode(text.encode()).decode()
                print(f"\nHasil decode: {decoded}")
            except:
                print("Error: Teks tidak valid untuk decode base64")
                
        elif choice == '3':
            print("Keluar dari program...")
            break
            
        else:
            print("Pilihan tidak valid, coba lagi")

if __name__ == "__main__":
    print("=== Program Encode/Decode Sederhana ===")
    main()
