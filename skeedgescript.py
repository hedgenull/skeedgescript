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

val = 0


def interpret(i: str, is_file: bool = False, last_goto: int = 0):
    """Interpret SkeedgeScript code."""

    global val
    tokens = i.split()

    for o, t in enumerate(tokens):
        match t:
            case "skeedge":
                val = 0
            case "SKEEDGE":
                val = 1
            case "Skeedge":
                val += 1
            case "skeedgE":
                val -= 1
            case "SKeedge":
                val += 2
            case "skeedGE":
                val -= 2
            case "sKeedge":
                val = -val
            case "skeedGe":
                val = +val
            case "skeEdge":
                print(val)
            case "SKEeDGE":
                print(chr(val), end="") if is_file else print(chr(val))
            case "SkeedgE":
                if tokens[o + 1].isdigit():
                    val += int(tokens[o + 1])
            case "sKEEDGe":
                if tokens[o + 1].isdigit():
                    val -= int(tokens[o + 1])
            case "SkEeDgE":
                if tokens[o + 1].isdigit():
                    val = int(tokens[o + 1])
            case "sKeEdGe":
                i = input("")
                if i.isdigit():
                    val = int(i)
                else:
                    val = ord(i[0])
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
