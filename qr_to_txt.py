import sys
import cv2

def qr_to_text(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(img)

    if data:
        print("Decoded text:\n")
        print(data)
    else:
        print("No QR code found or decoding failed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qr_to_txt.py <qr_image.png>")
    else:
        qr_to_text(sys.argv[1])
