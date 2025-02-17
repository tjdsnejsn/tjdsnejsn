from cryptography.fernet import Fernet

# Function to generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the generated key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt the .txt file
def encrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    with open(file_name, "wb") as file:
        file.write(encrypted_data)
    print(f"{file_name} encrypted successfully.")

# Function to decrypt the .txt file
def decrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    print(f"{file_name} decrypted successfully.")

# Main execution
if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()
        print("Key generated successfully.")
    elif choice == "2":
        file_name = input("Enter the name of the txt file to encrypt: ")
        encrypt_file(file_name)
    elif choice == "3":
        file_name = input("Enter the name of the txt file to decrypt: ")
        decrypt_file(file_name)
    else:
        print("Invalid choice. Exiting.")
