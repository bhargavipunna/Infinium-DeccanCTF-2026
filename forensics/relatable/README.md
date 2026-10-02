# Relatable (Forensics - 50 pts)

## Challenge Description
> A cringe-worthy joke hides a secret. Don't let the reality check distract you, dig into your life after this meme.  
> **Author:** SoggyBiscuit28  
> **File:** `reality.png`

---

## Analysis

The file `reality.png` is a standard 500x563 8-bit RGB PNG image showing a SpongeBob meme ("Break time!").

1. Checking the file structure shows standard chunks (`IHDR`, `iCCP`, `IDAT`, `IEND`) with no trailing data after `IEND`.
2. Analyzing the pixel values after de-filtering PNG scanlines reveals Least Significant Bit (LSB) steganography in bit 0 of the pixel color planes (R, G, and B channels).
3. The extracted LSB stream in MSB order starts with a 4-byte big-endian length prefix:
   ```text
   \x00\x00\x00\x17 -> 23 bytes
   ```
   Followed by the 23-byte ASCII flag:
   ```text
   0x1337{pr0cr4stin4t1on}
   ```

---

## Solution Script

Run:
```bash
python3 solve.py
```

### Flag
```text
0x1337{pr0cr4stin4t1on}
```
