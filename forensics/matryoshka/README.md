# Matryoshka (Forensics - 50 pts)

## Challenge Description
> An image was recovered from a suspect's system. Can you uncover what's inside?  
> **Author:** raghav aggarwal  
> **File:** `challenge.png`

---

## Analysis

The challenge title "Matryoshka" hints at nested files (Russian nesting dolls).

1. Inspecting `challenge.png` shows 100,158 trailing bytes after the PNG `IEND` chunk.
2. The trailing data begins with `00 00 00 00 00 10 JFIF...`. Replacing the zeroed-out header with the standard JPEG magic bytes `FF D8 FF E0` recovers a valid JPEG image.
3. The outer image depicts Ye Wenjie at the Red Coast Base, while the carved inner image depicts the Trisolaran fleet (both from Liu Cixin's sci-fi masterpiece *The Three-Body Problem*).
4. Inspecting the EXIF metadata of the carved image reveals a 2052-character hex-encoded string stored in `ImageDescription` / `UserComment`.
5. XOR-decrypting this hex string with the key `cixin` (the author's name) unveils the secret message and flag:
   ```text
   0x1337{0nly_4dv4nc3}
   ```
   *(referencing Thomas Wade's famous motto: "Only advance!")*

---

## Solution Script

Run:
```bash
python3 solve.py
```

### Flag
```text
0x1337{0nly_4dv4nc3}
```
