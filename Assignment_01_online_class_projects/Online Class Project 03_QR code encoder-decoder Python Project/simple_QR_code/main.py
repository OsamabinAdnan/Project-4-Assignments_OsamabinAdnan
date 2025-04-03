# Import the qrcode library for generating QR codes
import qrcode

# Define the data/text that will be encoded in the QR code
data = 'This is simple QR code from Osama bin Adnan'

# Create a QR code image from the data
# The make() function handles the encoding and image generation
img = qrcode.make(data)

# Save the generated QR code as a PNG image file
img.save('qrcode.png')