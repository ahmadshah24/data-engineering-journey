import qrcode


url = input("Enter the URL to generate QR code: ")
file_name = input("Enter the file name to save the QR code (including .png extension): ")

if not file_name.endswith(".png"):
    file_name += ".png"

    
img = qrcode.make(url)
img.save(file_name)

