import qrcode

# WhatsApp chat link
whatsapp_link = "https://wa.me/<YOUR WHATSAPP NUMBER>?text=Hello"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(whatsapp_link)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("whatsapp_qr_code.png")
