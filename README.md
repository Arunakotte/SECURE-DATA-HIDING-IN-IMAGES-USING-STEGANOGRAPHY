Image Encryption Program
This Python program allows you to embed a secret message into an image file using a basic encryption technique. The secret message is encoded into the image's pixel values and saved as a new encrypted image. The program also saves the password used for encryption and the length of the message into separate text files for later use in decryption.

Features
Encrypt an Image: The program embeds a secret message into an image, modifying the pixel values to encode the message.
Password Protection: A password is provided to protect the encrypted image and is saved to a text file.
Message Length: The length of the secret message is saved in a separate text file.
Automatic Image Viewing: Once the image is encrypted, the program opens the image automatically (Windows only).
Prerequisites
Before running the program, make sure you have the following:

Python 3.x installed.
OpenCV library installed. You can install it using pip:
bash
Copy
pip install opencv-python
A valid image file to encrypt (JPEG or PNG).
Usage
Prepare the Files: Ensure you have the Python script and an image file ready for encryption.

Run the Script:

Open a terminal/command prompt.
Navigate to the folder where the Python script is located.
Run the script:
bash
Copy
python encrypt.py
The script will prompt you to enter the secret message you want to encode and the password you want to use for encryption.
Enter Secret Message and Password:

The script will ask for a secret message. Enter the message you want to hide inside the image.
Next, enter the password that will be used to protect the encrypted image.
Encrypted Image and Files:

The encrypted image will be saved as encryptedImage.jpg in the same directory.
The password used for encryption will be saved in a text file called password.txt.
The length of the secret message will be saved in a text file called message_length.txt.
Open the Encrypted Image: Once the image is encrypted, the script will automatically open the image using the default image viewer on your system (works for Windows).
This Python program allows you to decrypt an image that was encrypted using a basic encryption technique. The secret message embedded within the image is retrieved by using the correct password and message length.

Features
Decrypt an Image: This program extracts the secret message hidden in an encrypted image by using the correct password and message length.
Password Protection: The program verifies the provided password before attempting to decrypt the image.
Message Retrieval: It retrieves and displays the original secret message encoded in the image.
Prerequisites
Before running the program, ensure you have the following:

Python 3.x installed.
OpenCV library installed. You can install it using pip:
bash
Copy
pip install opencv-python
The encrypted image file (encryptedImage.jpg).
The password file (password.txt) and message length file (message_length.txt), which are generated during encryption.
Usage
Prepare the Files: Ensure you have the Python script, the encrypted image, and the password and message length files created during encryption.

Run the Script:

Open a terminal/command prompt.
Navigate to the folder where the Python script is located.

Run the script:
bash
Copy
python decrypt.py
Enter Password:

The program will prompt you to enter the password for decryption.
If the password matches the one used during encryption, the message will be decrypted and displayed.

NOTE:
If you want to run this code on your system or desktop, you can change my image path to your system or desktop image path, then only the code will work on your system.
