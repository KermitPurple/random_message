#!/usr/bin/env python3
import sys, random

def gen_bytes(seed: int, message: str) -> bytearray:
    random.seed(seed)
    res = bytearray()
    for ch in message:
        while not random.randrange(2):
            res.append(0)
        else:
            res.append(ord(ch) ^ random.randrange(256))
    return res

def main():
    '''Driver Code'''
    _ = sys.argv.pop(0)
    if len(sys.argv) == 2:
        seed = int(sys.argv[0])
        message = sys.argv[1]
    else:
        print('Args to gen script must be seed and then message', file=sys.stderr)
        exit(1)
    print(gen_bytes(seed, message).hex(), end='')

if __name__ == '__main__':
    main()
