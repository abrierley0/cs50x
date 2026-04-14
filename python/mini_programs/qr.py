import qrcode

img = qrcode.make("https://google.com")
img.save("google_qrcode.png", "PNG")