import cv2
import os
import string
def decrypt_image(image_path, password, original_message_length, input_password):
    if password != input_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Encrypted image not found or cannot be opened.")
        return
    
    c = {i: chr(i) for i in range(255)}
    
    message = ""
    n, m, z = 0, 0, 0
    for _ in range(original_message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)

if __name__ == "__main__":
    try:
        with open("password.txt", "r") as file:
            saved_password = file.read().strip()
        with open("message_length.txt", "r") as file:
            message_length = int(file.read().strip())
    except FileNotFoundError:
        print("Error: Password or message length file not found. Encrypt an image first.")
        exit()

    input_password = input("Enter passcode for decryption: ")
    decrypt_image("encryptedImage.jpg", saved_password, message_length, input_password)

    input("Press Enter to exit...")
