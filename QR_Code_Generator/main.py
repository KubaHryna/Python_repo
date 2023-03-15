import qrcode
from random import randint

qr = qrcode.QRCode(
version=2,
error_correction=qrcode.ERROR_CORRECT_L,
box_size=randint(10, 20),
border=randint(4, 10)
 )
url = str(input("Podaj kod url do wygenerowania kodu QR: "))
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save('QR_code10.jpg')
