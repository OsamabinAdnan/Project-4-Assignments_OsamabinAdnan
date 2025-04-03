# Import required libraries
from pyzbar.pyzbar import decode  # For decoding QR codes and barcodes
from PIL import Image  # For opening and manipulating images

# Open the QR code image file
img = Image.open('images/qrcode.png')

# Decode the QR code from the image
# decode() returns a list of decoded objects containing data and type
result = decode(img)

# Print the decoded result
# The f-string formats the output with the decoded content
print(f"\nResult: {result}\n")
