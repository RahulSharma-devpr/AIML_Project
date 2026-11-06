import qrcode as qr
img =qr.make("https://youtube.com")
img.save("QR.png")