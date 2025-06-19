# Text ↔ QR Code Utility

Simple Python command-line tools to convert text files into QR codes and decode QR code images back to text.

---

## Features

- Encode `.txt` files as QR code images (`.png`)
- Decode QR code images back into the original text
- Fine-grained control over QR code settings:
  - Error correction level (`L`, `M`, `Q`, `H`)
  - QR version (1–40)
  - Box size (pixel scaling)
  - Border size (quiet zone)

---

## Requirements

Install dependencies:

```bash
pip install qrcode opencv-python
```

---

## Usage

### 1. Convert Text to QR

```bash
python txt_to_qr.py input.txt output.png [options]
```

**Options:**

| Flag              | Description                                  | Default |
|-------------------|----------------------------------------------|---------|
| `-e`, `--error`   | Error correction: `L`, `M`, `Q`, `H`          | `H`     |
| `-v`, `--version` | QR version (1–40). Use `None` for auto-fit   | `None`  |
| `-b`, `--box`     | Size of each box (in pixels)                 | `10`    |
| `-m`, `--margin`  | Border (quiet zone) size in boxes            | `4`     |

**Example:**

```bash
python txt_to_qr.py notes.txt qr.png -e L -v 40 -b 4 -m 2
```

---

### 2. Decode QR to Text

```bash
python qr_to_txt.py qr.png
```

Outputs the decoded text to the terminal.

---

## Notes

- Max QR version is **40**, corresponding to a 177×177 grid.
- Max storage (version 40, low EC): ~7,089 digits or ~2,953 bytes binary.
- Use low error correction and high version for max data capacity.

---

## License

MIT
