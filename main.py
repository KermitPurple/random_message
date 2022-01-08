#!/usr/bin/env python3
import random
random.seed(12345)
print(
    ''.join(chr(random.randrange(256) ^ c)
    for c in bytes.fromhex('40d200bc0050e100004b31000000008400e00064000000414500167300000b')
    if random.randrange(2)))
