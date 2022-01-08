#!/usr/bin/env python3
import sys, random

def gen_hex_str(seed: int, message: str) -> str:
    random.seed(seed)
    extra = random.Random()
    arr = bytearray()
    for ch in message:
        while not random.randrange(2):
            arr.append(extra.randrange(256))
        else:
            arr.append(ord(ch) ^ random.randrange(256))
    return arr.hex()

def gen_main_script(seed: int, message: str) -> str:
    return f'''#!/usr/bin/env python3
import random
random.seed({seed})
print(
    ''.join(chr(random.randrange(256) ^ c)
    for c in bytes.fromhex('{gen_hex_str(seed, message)}')
    if random.randrange(2)))
'''

def main():
    '''Driver Code'''
    _ = sys.argv.pop(0)
    if len(sys.argv) == 2:
        seed = int(sys.argv[0])
        message = sys.argv[1]
    else:
        print('Args to gen script must be seed and then message', file=sys.stderr)
        exit(1)
    print(gen_main_script(seed, message))

if __name__ == '__main__':
    main()
