# Import the qrcode library for generating QR codes
import qrcode

# Define the data/text to be encoded in the QR code
data = 'This is improved QR Code made by Osama bin Adnan'

# Create a QRCode instance with specified parameters
qr = qrcode.QRCode(
    version= 1,      # Version 1 creates a 21x21 matrix
    box_size= 10,    # Size of each box/pixel in the QR code
    border= 5        # Width of the border/quiet zone around the QR code
)

# Add the data to the QR code
qr.add_data(data)

# Generate the QR code and optimize its size if needed
qr.make(fit=True)

# Create the final image with custom colors
# fill_color: color of the QR code pattern
# back_color: background color
img = qr.make_image(fill_color='green', back_color='white')

# Save the QR code image as a PNG file
img.save('qrcode.png')