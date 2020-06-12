import qrcode

qr = qrcode.QRCode()
qr.add_data('智者千虑，必有一失。')
qr.make(fit=True)
image = qr.make_image()
image.convert('RGBA')

image.save('qr-code.png')
