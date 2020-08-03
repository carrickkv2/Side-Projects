import qrcode

image = qrcode.make('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
image.save('qr.png', 'PNG')