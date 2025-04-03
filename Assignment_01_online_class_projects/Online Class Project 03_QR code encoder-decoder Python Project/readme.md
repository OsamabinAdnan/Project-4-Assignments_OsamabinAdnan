# QR Code Encoder-Decoder Project

## Overview
A Python-based project for generating and decoding QR codes with basic and advanced features.

## Components

### 1. Simple QR Code Generator
Creates basic black and white QR codes with minimal configuration.

```python
import qrcode

data = 'This is simple QR code from Osama bin Adnan'
img = qrcode.make(data)
img.save('qrcode.png')
```

### 2. Improvised QR Code Generator
Enhanced QR code generation with customizable features:

- Configurable version and error correction
- Custom colors and size
- Adjustable border width

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Your text here')
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white")
img.save("qrcode.png")
```

### 3. QR Code Decoder
Reads and decodes QR code images using the `pyzbar` library.

## Requirements
- Python 3.x
- Dependencies:
  - `qrcode`
  - `pillow`
  - `pyzbar`

### Installation
```sh
pip install qrcode pillow pyzbar
```

## Project Structure
```
QR_Code_Project/
├── simple_QR_code/
│   ├── main.py
│   └── qrcode.png
├── improvised_QR_code/
│   ├── main.py
│   └── qrcode.png
└── decording_of_QR_code/
    ├── main.py
    └── images/
        └── qrcode.png
```

## Usage
### Generate Simple QR Code
```sh
cd simple_QR_code
python main.py
```

### Generate Improvised QR Code
```sh
cd improvised_QR_code
python main.py
```

### Decode QR Code
```sh
cd decording_of_QR_code
python main.py
```

## Output Files
- All QR codes are saved as PNG images.
- Simple QR codes are black and white.
- Improvised QR codes use green fill on a white background.

---

**Note:** Ensure all dependencies are installed before running the scripts.
