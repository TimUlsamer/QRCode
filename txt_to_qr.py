import sys
import qrcode

def txt_to_qr(input_path, output_path="output_qr.png", error_correction='H'):
    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.read()

    ec_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,  # ~7% redundancy
        'M': qrcode.constants.ERROR_CORRECT_M,  # ~15%
        'Q': qrcode.constants.ERROR_CORRECT_Q,  # ~25%
        'H': qrcode.constants.ERROR_CORRECT_H   # ~30%
    }
    ec = ec_levels.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_H)

    qr = qrcode.QRCode(
        version=None,  # auto size
        error_correction=ec,
        box_size=10,   # size of each box (pixel)
        border=4       # white border thickness
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(output_path)
    print(f"QR code saved to {output_path} with error correction: {error_correction.upper()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python txt_to_qr.py <input_file.txt> [output_image.png] [error_correction: L/M/Q/H]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output_qr.png"
        ec_level = sys.argv[3] if len(sys.argv) > 3 else 'H'
        txt_to_qr(input_file, output_file, ec_level)
