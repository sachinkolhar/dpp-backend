import base64

qr_base64 = "iVBORw0KGgoAAAANS..."

with open("qr.png", "wb") as f:
    f.write(base64.b64decode(qr_base64))

print("QR saved as qr.png")
