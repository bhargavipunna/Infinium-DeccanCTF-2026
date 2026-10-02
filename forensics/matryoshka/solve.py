#!/usr/bin/env python3
import re
import os

def solve(image_path="challenge.png"):
    if not os.path.exists(image_path):
        if os.path.exists(os.path.join("..", "..", image_path)):
            image_path = os.path.join("..", "..", image_path)

    with open(image_path, "rb") as f:
        data = f.read()

    # Find the end of PNG IEND chunk
    iend_pos = data.find(b"IEND")
    if iend_pos == -1:
        raise ValueError("IEND chunk not found")

    tail = data[iend_pos + 8:]  # 4 bytes IEND + 4 bytes CRC

    # Fix masked JPEG header: 00 00 00 00 -> FF D8 FF E0
    carved_jpeg = b"\xff\xd8\xff\xe0" + tail[4:]

    # Extract hex-encoded string from EXIF metadata
    hex_matches = re.findall(b"[a-fA-F0-9]{50,}", carved_jpeg)
    if not hex_matches:
        raise ValueError("Hex string not found in EXIF")

    raw_bytes = bytes.fromhex(hex_matches[0].decode("ascii"))

    # Theme: The Three-Body Problem (Liu Cixin)
    key = b"cixin"
    decrypted = bytes([raw_bytes[i] ^ key[i % len(key)] for i in range(len(raw_bytes))])
    flag = decrypted.split(b"\n")[0].decode("utf-8")
    print(f"Flag: {flag}")
    return flag

if __name__ == "__main__":
    solve()
