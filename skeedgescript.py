# ================================================================================>
# FILE NAME:  skeedgescript.py
#
# PURPOSE:
# SkeedgeScript interpreter written in Python 3.
#
# CREATED DATE: 2022-05-29
# AUTHOR:       @hedgenull (hedgefleming@gmail.com)
# ================================================================================>

import argparse

ACCUMULATOR = 0


def interpret(i: str, is_file: bool = False):
    """Interpret SkeedgeScript code."""

    global ACCUMULATOR
    tokens = i.split()

    for o, t in enumerate(tokens):
        match t:
            case "skeedge":
                ACCUMULATOR = 0
            case "SKEEDGE":
                ACCUMULATOR = 1
            case "Skeedge":
                ACCUMULATOR += 1
            case "skeedgE":
                ACCUMULATOR -= 1
            case "SKeedge":
                ACCUMULATOR += 2
            case "skeedGE":
                ACCUMULATOR -= 2
            case "skeedGe":
                ACCUMULATOR = +ACCUMULATOR
            case "skeEdge":
                print(ACCUMULATOR)
            case "SKEeDGE":
                print(chr(ACCUMULATOR), end="") if is_file else print(chr(ACCUMULATOR))
            case "SkeedgE":
                if tokens[o + 1].isdigit():
                    ACCUMULATOR += int(tokens[o + 1])
            case "sKEEDGe":
                if tokens[o + 1].isdigit():
                    ACCUMULATOR -= int(tokens[o + 1])
            case "SkEeDgE":
                if tokens[o + 1].isdigit():
                    ACCUMULATOR = int(tokens[o + 1])
            case "sKeEdGe":
                i = input("")
                if i.isdigit():
                    ACCUMULATOR = int(i)
                else:
                    ACCUMULATOR = ord(i[0])
            case "sKeedGe":
                if ACCUMULATOR > 0:
                    ACCUMULATOR = 0
                else:
                    ACCUMULATOR = 1
            case "SkEEDgE":
                if ACCUMULATOR > 0:
                    ACCUMULATOR = 1
                else:
                    ACCUMULATOR = 0
            case _ as err:
                if not is_file:
                    print(f"Error: Unknown command '{err}'")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="SkeedgeScript interpreter written in Python")
    ap.add_argument("-f", "--file", help="Path to SkeedgeScript source file")
    ap.add_argument(
        "-i", "--interactive", action="store_true", help="Enable interactive shell mode"
    )
    args = ap.parse_args()

    if args.interactive:
        while True:
            i = input("SkeedgeScript > ").strip()
            interpret(i)
    elif args.file:
        try:
            with open(args.file, "r") as f:
                code = f.read()
        except FileNotFoundError:
            print(f"File not found: {args.file}")
        else:
            interpret(code, is_file=True)
