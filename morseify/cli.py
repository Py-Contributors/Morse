# Entry point for the morse command line interface

import sys
import argparse

parser = argparse.ArgumentParser(description='Morse code encoder/decoder')
parser.add_argument('-t', '--text', help='Text to encode/decode')
parser.add_argument('-m', '--morse', help='Morse code to encode/decode')
parser.add_argument('-b', '--binary', help='Binary to encode/decode')

args = parser.parse_args()

if not any([args.text, args.morse, args.binary]):
    parser.print_help()
    sys.exit(1)

from morseify.main import Morseify

m = Morseify()


def main():
    if args.text:
        print(m.encode_morse(args.text))
    elif args.morse:
        print(m.decode_morse(args.morse))
    elif args.binary:
        print(m.binary_to_morse(args.binary))


if __name__ == '__main__':
    main()