import argparse
import qrcode

def txt_to_qr(input_path, output_path, error_correction, version, box_size, border):
    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.read()

    ec_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,  # ~7% error recovery
        'M': qrcode.constants.ERROR_CORRECT_M,  # ~15%
        'Q': qrcode.constants.ERROR_CORRECT_Q,  # ~25%
        'H': qrcode.constants.ERROR_CORRECT_H   # ~30%
    }

    qr = qrcode.QRCode(
        version=version,  # None = auto-fit
        error_correction=ec_levels[error_correction.upper()],
        box_size=box_size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(output_path)

    print(f"QR saved to {output_path}")
    print(f"Settings: version={version}, EC={error_correction.upper()}, box_size={box_size}, border={border}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a .txt file into a QR code PNG.")
    parser.add_argument("input_file", help="Path to the input .txt file")
    parser.add_argument("output_file", help="Path to the output .png file")
    parser.add_argument("-e", "--error", default="H", choices=["L", "M", "Q", "H"],
                        help="Error correction level (default: H)")
    parser.add_argument("-v", "--version", type=int, default=None,
                        help="QR version (1–40). Default: auto-size")
    parser.add_argument("-b", "--box", type=int, default=10,
                        help="Box size in pixels (default: 10)")
    parser.add_argument("-m", "--margin", type=int, default=4,
                        help="Border (quiet zone) size in boxes (default: 4)")

    args = parser.parse_args()

    txt_to_qr(
        input_path=args.input_file,
        output_path=args.output_file,
        error_correction=args.error,
        version=args.version,
        box_size=args.box,
        border=args.margin
    )
