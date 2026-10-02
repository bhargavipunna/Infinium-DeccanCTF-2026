# Infinium DeccanCTF 2026 - Writeups & Solutions

This repository contains writeups, analysis, and automated solver scripts for challenges solved during **Infinium DeccanCTF 2026**.

---

## Solved Challenges

| Category | Challenge | Points | Solved | Flag |
| :--- | :--- | :--- | :--- | :--- |
| **Forensics** | [Relatable](forensics/relatable/) | 50 | Yes | `0x1337{pr0cr4stin4t1on}` |
| **Forensics** | [Matryoshka](forensics/matryoshka/) | 50 | Yes | `0x1337{0nly_4dv4nc3}` |
| **Cryptography** | [easyrsa](crypto/easyrsa/) | 73 | Yes | `0x1337{w4snt_s0_h4rd_r1ght_b0ttyb0y4}` |

---

## Challenge Summaries

### 1. [Relatable (Forensics - 50 pts)](forensics/relatable/)
- **Description:** A SpongeBob meme with the caption *"A cringe-worthy joke hides a secret. Don't let the reality check distract you, dig into your life after this meme."*
- **Vulnerability / Technique:** LSB (Least Significant Bit) steganography in PNG pixel data across RGB color channels (MSB bit order).
- **Flag:** `0x1337{pr0cr4stin4t1on}`

### 2. [Matryoshka (Forensics - 50 pts)](forensics/matryoshka/)
- **Description:** Recovered image from a suspect system.
- **Vulnerability / Technique:** Hidden JPEG appended after the PNG `IEND` chunk with corrupted magic bytes (`00 00 00 00` instead of `FF D8 FF E0`). The carved image contains EXIF metadata with a hex string that was XOR encrypted using key `cixin` (*The Three-Body Problem* theme).
- **Flag:** `0x1337{0nly_4dv4nc3}`

### 3. [easyrsa (Cryptography - 73 pts)](crypto/easyrsa/)
- **Description:** An RSA challenge with modulus $p$ (3000 bits), exponent $e = 65536 = 2^{16}$, and ciphertext $c$.
- **Vulnerability / Technique:** 
  1. Multi-prime RSA ($p = p_1 \cdot p_2 \cdot p_3$).
  2. $p_1$ was found on FactorDB.
  3. $p_2 \cdot p_3$ factored using Fermat's factorization method ($p_3 - p_2 = 318$).
  4. Decryption using 16 sequential modular square roots modulo $p_2 \equiv 3 \pmod 4$.
- **Flag:** `0x1337{w4snt_s0_h4rd_r1ght_b0ttyb0y4}`
