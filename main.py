#!/usr/bin/env python3
import random
random.seed(42069)
print(
    ''.join(chr(random.randrange(256) ^ c)
    for c in bytes.fromhex('d6439a5c9439d29bcac33d90ae69ed01c4')
    if random.randrange(2)))
