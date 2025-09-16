import qrcode
from PIL import Image

# Datos del QR
url = 'www.github.com/IvanDaGomez/chatGPTDesdeCero'
text = 'GPTFromScratch'
# Ruta del logo
logo_path = "QRs/WhatsApp.png"

# Crea el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores (permite poner logo)
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Crea la imagen QR
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# # Abre el logo
logo = Image.open(logo_path)

# Calcula el tamaño del logo (ej. 15% del tamaño del QR)
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.2)
logo = logo.resize((logo_size, logo_size))

# Calcula posición centrada
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Pega el logo sobre el QR
# qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Guarda el resultado
qr_img.save("QRs/" + text + '.png')
