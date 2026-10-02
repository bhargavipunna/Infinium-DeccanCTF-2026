#!/usr/bin/env python3
import math
import re
import os

def solve(chall_file="chall.txt"):
    if not os.path.exists(chall_file):
        if os.path.exists(os.path.join("..", "..", chall_file)):
            chall_file = os.path.join("..", "..", chall_file)
        elif os.path.exists("chall 2.txt"):
            chall_file = "chall 2.txt"

    with open(chall_file, "r") as f:
        text = f.read()

    p = int(re.search(r"p\s*=\s*(\d+)", text).group(1))
    e = int(re.search(r"e\s*=\s*(\d+)", text).group(1))
    c = int(re.search(r"c\s*=\s*(\d+)", text).group(1))

    # Prime factor 1 obtained from FactorDB
    p1 = 5748299135649819615715196329232902039563988139662386101035735408977294828850416061432485452896522482685812364857926078543884298837052019183435057851218285036742567969905264247637496736965258248752990615665892556700912143415272784862714828998253802744990988964881054037146094733412556002802245391941633
    f2 = p // p1

    # Fermat's factorization on remaining 2000-bit factor f2 = p2 * p3
    a = math.isqrt(f2)
    if a * a < f2:
        a += 1
    diff = (a * a) - f2
    b = math.isqrt(diff)
    p2 = a - b
    p3 = a + b
    assert p2 * p3 == f2

    # p2 % 4 == 3, so square root of x mod p2 is x^((p2+1)//4) mod p2
    curr = c % p2
    for step in range(16):
        r = pow(curr, (p2 + 1) // 4, p2)
        r1 = r
        r2 = p2 - r
        if step < 15:
            # Pick the quadratic residue
            curr = r1 if pow(r1, (p2 - 1) // 2, p2) == 1 else r2
        else:
            for cand in [r1, r2]:
                cand_bytes = cand.to_bytes((cand.bit_length() + 7) // 8, "big")
                if b"0x1337{" in cand_bytes:
                    flag = cand_bytes.decode("ascii")
                    print(f"Flag: {flag}")
                    return flag

if __name__ == "__main__":
    solve()
