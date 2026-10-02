# easyrsa (Cryptography - 73 pts)

## Challenge Description
> It’s called easy rsa. Someone’s probably seen these primes before, right ;3  
> **File:** `chall.txt`

---

## Analysis

We are given:
- Modulus $p$ (2999 bits)
- Public exponent $e = 65536 = 2^{16}$
- Ciphertext $c$

### 1. Factorization
The emoticon `";3"` in the challenge description hints at a 3-prime modulus ($p = p_1 \cdot p_2 \cdot p_3$).
- Looking up $p$ on **FactorDB** yields the first 1000-bit prime factor $p_1$:
  ```text
  p1 = 5748299135649819615715196329232902039563988139662386101035735408977294828850416061432485452896522482685812364857926078543884298837052019183435057851218285036742567969905264247637496736965258248752990615665892556700912143415272784862714828998253802744990988964881054037146094733412556002802245391941633
  ```
- The remaining 2000-bit quotient $f_2 = p / p_1 = p_2 \cdot p_3$ factors immediately via **Fermat's Factorization Method**, because $p_2$ and $p_3$ are very close ($p_3 - p_2 = 318$).

### 2. Decryption
Because $m$ is short ($< 1000$ bits), $m < p_2$, which means $m \equiv c^{1/65536} \pmod{p_2}$.
- $p_2 \equiv 3 \pmod 4$, so quadratic residues mod $p_2$ have square roots $r = x^{(p_2 + 1)/4} \pmod{p_2}$.
- Since $\left(\frac{-1}{p_2}\right) = -1$, exactly one of $\pm r$ is a quadratic residue.
- Applying 16 sequential modular square roots (always selecting the quadratic residue at steps 1 through 15) narrows the candidate values down to just two roots at step 16, yielding the ASCII flag:
  ```text
  0x1337{w4snt_s0_h4rd_r1ght_b0ttyb0y4}
  ```

---

## Solution Script

Run:
```bash
python3 solve.py
```

### Flag
```text
0x1337{w4snt_s0_h4rd_r1ght_b0ttyb0y4}
```
