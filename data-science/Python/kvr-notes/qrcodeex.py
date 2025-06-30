import qrcode  
# generating a QR code using the make() function  
qr_img = qrcode.make("Welcome to KVR  Python Classes.")  
# saving the image file  
qr_img.save("kvr-img.jpg")  