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

def main():
    '''Driver Code'''
    _ = sys.argv.pop(0)
    if len(sys.argv) == 2:
        seed = int(sys.argv[0])
        message = sys.argv[1]
    else:
        print('Args to gen script must be seed and then message', file=sys.stderr)
        exit(1)
    print(gen_hex_str(seed, message), end='')

if __name__ == '__main__':
    main()
