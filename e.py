import cv2
import os
import string
def encrypt_image(image_path, message, password, output_path="encryptedImage.jpg"):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found or cannot be opened.")
        return None
    
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # Open the image on Windows
    return password

if __name__ == "__main__":
    image_path = r"C:\Users\nymak\OneDrive\Desktop\1234.jpg"
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    saved_password = encrypt_image(image_path, message, password)

    if saved_password:
        with open("password.txt", "w") as file:
            file.write(saved_password)
        with open("message_length.txt", "w") as file:
            file.write(str(len(message)))

    print("Encryption complete. Run `decrypt.py` to decrypt the image.")
