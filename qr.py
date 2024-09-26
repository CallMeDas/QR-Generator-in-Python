
# First we have to install qrcode libaray.. for that use below command.
# pip install qrcode


import qrcode

qr= qrcode.make("https://github.com/CallMeDas")  # you can use your own link and run the code to genreate QR.
qr.save("qr.jpg")

