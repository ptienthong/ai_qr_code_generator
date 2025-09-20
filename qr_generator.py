import qrcode

def generate_qr(url: str, filename: str = "qrcode.png"):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size (1 = 21x21, larger numbers = bigger QR)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,     # thickness of border (minimum is 4)
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    user_url = input("Enter the URL to generate a QR code: ")
    generate_qr(user_url)
