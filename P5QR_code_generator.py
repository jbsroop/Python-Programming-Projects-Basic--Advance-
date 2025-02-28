import qrcode
data = input('Enter the text or URL:').strip()
filename =input('Enter the filename:').strip()
Qr = qrcode.QRCode(box_size=10,border=4)
Qr.add_data(data)
image = Qr.make_image(fill_color = 'black', back_color ='white')
image.save(filename)
print(f'QR code saved as {filename}')