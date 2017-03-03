import Stack
import sys
import argparse

def main():
    ''' Argument parsing '''
    mainparser = argparse.ArgumentParser()
    mainparser.add_argument("echo")
    args = mainparser.parse_args()
    print(args.echo)

    return 0

if __name__ == "__main__":
    main()