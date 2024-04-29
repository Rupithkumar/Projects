import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,border=4,box_size=10)
qr.add_data("https://www.rolls-roycemotorcars.com/en_GB/home.html")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="red")
img.save("Rolls Royce color.png")