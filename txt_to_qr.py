import sys
import qrcode

def txt_to_qr(input_path, output_path="output_qr.png", error_correction='H'):
    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.read()

    ec_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }
    ec = ec_levels.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_H)

    qr = qrcode.QRCode(error_correction=ec)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(output_path)
    print(f"QR code saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python txt_to_qr.py <input_file.txt> [output_image.png]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output_qr.png"
        txt_to_qr(input_file, output_file)
