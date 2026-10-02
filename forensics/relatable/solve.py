#!/usr/bin/env python3
import zlib
import os

def solve(image_path="reality.png"):
    if not os.path.exists(image_path):
        # Look in current or parent directory
        if os.path.exists(os.path.join("..", "..", image_path)):
            image_path = os.path.join("..", "..", image_path)

    with open(image_path, "rb") as f:
        data = f.read()

    idat = b""
    offset = 8
    while offset < len(data):
        length = int.from_bytes(data[offset:offset+4], "big")
        ctype = data[offset+4:offset+8]
        if ctype == b"IDAT":
            idat += data[offset+8:offset+8+length]
        offset += 12 + length

    raw = zlib.decompress(idat)
    width, height, bpp = 500, 563, 3
    stride = 1 + width * bpp

    recon = bytearray(height * width * bpp)
    for y in range(height):
        filter_type = raw[y * stride]
        for x in range(width * bpp):
            recon_x = y * width * bpp + x
            raw_val = raw[y * stride + 1 + x]
            a = recon[recon_x - bpp] if x >= bpp else 0
            b_val = recon[recon_x - width * bpp] if y > 0 else 0
            c = recon[recon_x - width * bpp - bpp] if (y > 0 and x >= bpp) else 0

            if filter_type == 0:
                val = raw_val
            elif filter_type == 1:
                val = (raw_val + a) & 0xff
            elif filter_type == 2:
                val = (raw_val + b_val) & 0xff
            elif filter_type == 3:
                val = (raw_val + ((a + b_val) >> 1)) & 0xff
            elif filter_type == 4:
                p = a + b_val - c
                pa, pb, pc = abs(p - a), abs(p - b_val), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b_val if pb <= pc else c)
                val = (raw_val + pr) & 0xff
            else:
                val = raw_val
            recon[recon_x] = val

    # Extract LSB of RGB channels
    bits = [recon[i] & 1 for i in range(0, len(recon), 3)]
    out = bytearray()
    for i in range(0, 8 * 100, 8):
        byte = 0
        for b in range(8):
            byte = (byte << 1) | bits[i + b]
        out.append(byte)

    flag_len = int.from_bytes(out[:4], "big")
    flag = out[4:4+flag_len].decode("ascii", errors="replace")
    print(f"Flag: {flag}")
    return flag

if __name__ == "__main__":
    solve()
