#!/usr/bin/env python3
import sys, random

def gen_hex_str(seed: int, message: str) -> str:
    '''
    generate a hex string that can be used to output message
    when using the same seed
    :seed: int; the seed to be passed to random.seed function
    :message: str; the message to be encoded into a hex string
    '''
    random.seed(seed)
    extra = random.Random()
    arr = bytearray()
    for ch in message:
        while not random.randrange(2):
            arr.append(extra.randrange(256))
        else:
            arr.append(ord(ch) ^ random.randrange(256))
    return arr.hex().upper()

def gen_main_script(seed: int, message: str) -> str:
    '''
    generate a script that will output the message
    :seed: int; the seed to be passed to random.seed function
    :message: str; the message to be encoded into a hex string
    '''
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
